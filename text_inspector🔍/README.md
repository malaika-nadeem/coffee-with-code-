# Text Inspector 🔍

A Streamlit web app that reads any document and tells you everything about it — word count, character count, sentence count, and top 10 most frequent words visualized as a bar chart.

---

## What it does

- Upload a `.txt`, `.pdf`, `.docx`, or `.pptx` file
- Extracts text from the document
- Displays file stats — words, characters, sentences
- Shows top 10 most frequent words as a bar chart
- Download the summary report as a `.txt` file

---

## Built with

| Library | Purpose |
|---|---|
| `streamlit` | Build the web app UI |
| `pdfplumber` | Extract text from PDF files |
| `python-docx` | Extract text from Word files |
| `python-pptx` | Extract text from PowerPoint files |
| `re` | Split text into sentences |
| `collections.Counter` | Count word frequency |
| `io` | Handle uploaded files in memory |

---

## How to run

**1. Clone the repo**
```bash
git clone https://github.com/coffee-with-code/text-inspector.git
cd text-inspector
```

**2. Install dependencies**
```bash
pip install streamlit pdfplumber python-docx python-pptx
```

**3. Run the app**
```bash
streamlit run app.py
```

---

## What I learned

- File handling across multiple document formats
- How documents are just text underneath different wrappers
- Working with in-memory file streams using `io.BytesIO`
- Building interactive UIs with Streamlit

---

*Built by Malaika ^_____^
