import os
import tempfile

import faiss
import numpy as np
import requests
import streamlit as st
from pypdf import PdfReader

st.set_page_config(page_title="AI Dokumentový Asistent (RAG)", page_icon="📄")
st.title("📄 AI Dokumentový Asistent (RAG)")
st.write("Nahraj PDF dokument a zeptej se na jeho obsah.")

OLLAMA_URL = "http://localhost:11434"


def extract_text_from_pdf(pdf_path: str) -> str:
    reader = PdfReader(pdf_path)
    text_parts = []

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text_parts.append(page_text)

    return "\n".join(text_parts)


def split_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> list[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks


def get_embedding(text: str) -> list[float]:
    response = requests.post(
        f"{OLLAMA_URL}/api/embeddings",
        json={
            "model": "nomic-embed-text",
            "prompt": text
        },
        timeout=120
    )
    response.raise_for_status()
    return response.json()["embedding"]


def get_embeddings(texts: list[str]) -> np.ndarray:
    embeddings = [get_embedding(text) for text in texts]
    return np.array(embeddings, dtype="float32")


def build_faiss_index(embeddings: np.ndarray):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index


def search_similar_chunks(question: str, chunks: list[str], index, k: int = 4) -> list[str]:
    question_vector = np.array([get_embedding(question)], dtype="float32")
    distances, indices = index.search(question_vector, k)

    results = []
    for i in indices[0]:
        if 0 <= i < len(chunks):
            results.append(chunks[i])

    return results


def ask_llm(question: str, context_chunks: list[str]) -> str:
    context = "\n\n---\n\n".join(context_chunks)

    prompt = f"""
Použij pouze informace z poskytnutého kontextu.
Pokud odpověď v kontextu není, napiš: "Tohle v dokumentu nemohu spolehlivě najít."

KONTEXT:
{context}

OTÁZKA:
{question}
"""

    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        },
        timeout=180
    )
    response.raise_for_status()
    return response.json()["response"]


uploaded_file = st.file_uploader("Nahraj PDF", type=["pdf"])

if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "index" not in st.session_state:
    st.session_state.index = None

if uploaded_file is not None:
    with st.spinner("Zpracovávám PDF..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        full_text = extract_text_from_pdf(tmp_path)
        os.remove(tmp_path)

        if not full_text.strip():
            st.error("Z PDF se nepodařilo načíst žádný text.")
            st.stop()

        chunks = split_text(full_text)
        embeddings = get_embeddings(chunks)
        index = build_faiss_index(embeddings)

        st.session_state.chunks = chunks
        st.session_state.index = index

    st.success("PDF je připravené. Můžeš se ptát.")

question = st.text_input("Zeptej se na dokument")

if question and st.session_state.chunks is not None and st.session_state.index is not None:
    with st.spinner("🤖 AI přemýšlí..."):
        relevant_chunks = search_similar_chunks(
            question,
            st.session_state.chunks,
            st.session_state.index
        )
        answer = ask_llm(question, relevant_chunks)

    st.subheader("💡 Odpověď")
    st.markdown(answer)

    with st.expander("📚 Zdroje (části dokumentu použité pro odpověď)"):
        for i, chunk in enumerate(relevant_chunks, start=1):
            st.markdown(f"**📄 Úryvek {i}:**")
            st.info(chunk[:500] + "...")