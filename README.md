📄 AI Dokumentový Asistent (RAG)

Jednoduchá AI aplikace pro práci s PDF dokumenty.
Uživatel nahraje dokument a může se na něj ptát pomocí přirozeného jazyka.

Projekt využívá lokální AI modely přes Ollama a implementuje princip RAG (Retrieval-Augmented Generation).

🎯 Use Case

Tento nástroj simuluje interní AI řešení ve firmě nebo organizaci, kde uživatelé potřebují rychle vyhledávat informace v dokumentech (např. směrnice, manuály, pravidla).

Cílem je:

zrychlit práci s dokumenty
snížit manuální hledání
zpřístupnit informace pomocí přirozeného jazyka
🚀 Funkce
📄 nahrání PDF dokumentu
🔍 vyhledávání relevantních částí textu
🤖 odpovědi pomocí lokálního LLM (Ollama)
📚 zobrazení zdrojových úryvků
⚡ rychlé vyhledávání pomocí FAISS
🧠 Jak projekt funguje
PDF se načte pomocí pypdf
text se rozdělí na menší části (chunks)
každá část se převede na embedding
embeddingy se uloží do FAISS indexu
při dotazu se najdou nejrelevantnější části dokumentu
tyto části se použijí jako kontext pro odpověď modelu
🧩 Co je RAG

RAG (Retrieval-Augmented Generation) je přístup, kdy se modelu neposílá celý dokument, ale pouze relevantní části nalezené pomocí vyhledávání.

Výhody:

přesnější odpovědi
lepší práce s většími dokumenty
větší kontrola nad zdroji informací
🛠️ Technologie
Python
Streamlit
FAISS
Ollama
llama3.2
nomic-embed-text
PyPDF
requests
numpy
▶️ Instalace

Nejprve vytvoř a aktivuj virtuální prostředí.

Windows
python -m venv venv
venv\Scripts\activate

Poté nainstaluj závislosti:

pip install -r requirements.txt
🤖 Instalace Ollama

Stáhni a nainstaluj Ollamu:

https://ollama.com/download

Stáhni potřebné modely:

ollama pull llama3.2
ollama pull nomic-embed-text
▶️ Spuštění aplikace

Ujisti se, že běží Ollama, poté spusť:

streamlit run app.py

Aplikace poběží na:

http://localhost:8501
💡 Ukázka použití

Příklady dotazů:

O čem je dokument?
Shrň hlavní body
Jaké jsou podmínky?
Co dokument říká o konkrétním tématu?
🔮 Možná rozšíření
historie chatu
práce s více dokumenty
přesnější chunking
citace včetně čísla stránky
deployment (cloud)
lepší UI
👨‍💻 Autor

Rogan
