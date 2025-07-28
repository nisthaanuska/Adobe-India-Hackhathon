# PDF Outline Extractor (Round 1A)

## 📂 Input & Output Directories

- **Input Directory:** `Round1A/input/`  
  Place your PDF files here (each ≤ 50 pages).
  
- **Output Directory:** `Round1A/output/`  
  Extracted JSON outlines will be saved here, one per PDF.

## 🎯 Objective

Extract a structured outline from a PDF, including:

- Document Title
- Headings (H1, H2, H3) with their page numbers

## 📥 Input

- **Folder:** `/app/input/`
- **Format:** One or more PDFs (each ≤ 50 pages)

## 📤 Output

- **Folder:** `/app/output/`
- **Format:** One JSON per PDF  
  Example:

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

## 🚀 Usage

1. Place PDFs in `/app/input/`.
2. Run the Docker container (see `Dockerfile` for details).
3. Extracted outlines will appear in `/app/output/` as JSON files.

## 🛠️ Technology Stack

- **Python 3.10+**
  - [`PyMuPDF (fitz)`](https://pymupdf.readthedocs.io/)
  - *(Optional)* `spaCy` for fallback NLP
- **Docker** (amd64, CPU only)

## 📁 Folder Structure

```
Round1A/
├── input/                  # <--- Input PDFs directory
├── output/                 # <--- Output JSONs directory
├── main.py                 # Entry point
├── utils/
│   └── extractor.py        # PDF parsing and heading extraction logic
├── Dockerfile
├── requirements.txt
└── README.md
```
