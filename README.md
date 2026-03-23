# AI Dokumentový Asistent (RAG)

Jednoduchá AI aplikace pro práci s PDF dokumenty.  
Uživatel nahraje PDF a může se na něj ptát přirozeným jazykem.

Projekt využívá princip **RAG (Retrieval-Augmented Generation)**:
- dokument se načte a rozdělí na menší části,
- části se převedou na embeddingy,
- embeddingy se uloží do FAISS indexu,
- při dotazu se najdou relevantní úryvky,
- ty se předají lokálnímu LLM přes Ollama.

## Funkce

- nahrání PDF dokumentu
- dotazy nad obsahem dokumentu
- vyhledání relevantních částí textu
- odpovědi generované lokálním LLM
- zobrazení použitých zdrojových úryvků

## Použité technologie

- Python
- Streamlit
- FAISS
- Ollama
- llama3.2
- nomic-embed-text
- PyPDF
- requests
- numpy

## Jak projekt funguje

1. PDF se načte pomocí `pypdf`
2. text se rozdělí na menší části
3. každá část se převede na embedding
4. embeddingy se uloží do FAISS
5. při dotazu se najdou nejrelevantnější části dokumentu
6. tyto části se použijí jako kontext pro odpověď modelu

## Instalace

Nejprve vytvoř a aktivuj virtuální prostředí.

### Windows
```bash
python -m venv venv
venv\Scripts\activate

Potom nainstaluj závislosti:

pip install -r requirements.txt
Instalace Ollama

Stáhni a nainstaluj Ollamu:

https://ollama.com/download

Stáhni potřebné modely:

ollama pull llama3.2
ollama pull nomic-embed-text
Spuštění aplikace

Nejprve se ujisti, že běží Ollama.

Potom spusť:

streamlit run app.py

Aplikace poběží typicky na:

http://localhost:8501
Ukázka použití

Příklady dotazů:

O čem je dokument?
Shrň hlavní body.
Jaké jsou podmínky nebo pravidla?
Co dokument říká o konkrétní disciplíně nebo tématu?
Možná vylepšení
historie chatu
více dokumentů najednou
přesnější chunking
citace se stránkou dokumentu
nasazení online
filtrování a správa dokumentů
Proč jsem projekt vytvořil

Cílem bylo postavit jednoduchý interní AI nástroj pro práci s dokumenty, který ukazuje praktické použití:

LLM
RAG
vyhledávání v datech
automatizaci práce s dokumenty
Autor

Tomáš Rogan


## Pak udělej commit
Ve VS Code terminálu:

```bash
git add README.md
git commit -m "Add project README"
git push
