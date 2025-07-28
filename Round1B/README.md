# Persona-Driven Document Intelligence (Round 1B)

> **Rethink Reading. Rediscover Knowledge.**  
Transform static PDFs into an intelligent, interactive experience. This solution extracts, ranks, and surfaces the most relevant sections from a collection of documents—tailored to a specific persona and their job-to-be-done.

---

## 🚀 Features

- **Persona-Aware Extraction**: Surfaces what matters most for each user and task.  
- **Multi-Document Support**: Handles 3–10 PDFs per test case, across any domain.  
- **Contextual Ranking**: Prioritizes sections using persona/job-driven relevance.  
- **Modular & Extensible**: Easy to adapt for new domains, personas, or advanced NLP.  
- **Offline & Secure**: Runs fully offline, with no network dependencies.

---

## 📥 Input

Each test case folder (e.g., `TestCase1_AcademicResearch/`) must contain:

- `input.json` — Specifies:
  - `persona`: Role and focus areas (e.g., "PhD Researcher in Computational Biology")
  - `job_to_be_done`: The concrete task (e.g., "Prepare a literature review...")
  - `documents`: List of PDF file paths (relative to the test case folder)
- `pdfs/` — Subfolder containing the referenced PDFs

**Example `input.json`:**

```json
{
  "persona": {
    "role": "PhD Researcher in Computational Biology",
    "focus_areas": ["methodologies", "datasets", "performance benchmarks"]
  },
  "job_to_be_done": "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks.",
  "documents": [
    "pdfs/Research1.pdf",
    "pdfs/Research2.pdf"
  ]
}
```

---

## 📤 Output

For each test case, an `output.json` is generated in the same folder, containing:

- **Metadata**: Input docs, persona, job, timestamp  
- **Extracted Sections**: Ranked by relevance, with section title, page, and importance rank

---

## 🛠️ Usage

1. **Organize Test Cases**  
   Place each test case folder (with `input.json` and `pdfs/`) inside `Round1B/`.

2. **Build Docker Image**
   ```sh
   docker build --platform linux/amd64 -t round1b_solution:latest .
   ```

3. **Run the Solution**
   ```sh
   docker run --rm -v "$(pwd):/app" --network none round1b_solution:latest
   ```

   All test cases will be processed; each will get its own `output.json`.

---

## 🧩 Folder Structure

```
Round1B/
├── main.py                         # Entry point
├── utils/
│   ├── extractor.py                # PDF parsing and section extraction
│   └── relevance.py                # Relevance scoring logic
├── TestCase1_AcademicResearch/
│   ├── input.json
│   └── pdfs/
├── ... (other test cases)
├── Dockerfile
├── requirements.txt
├── README.md
└── approach_explanation.md
```

---

## 🔍 Extensibility

- **Semantic Ranking**: Integrate spaCy or transformer models for deeper relevance  
- **Sub-section Analysis**: Expand to extract and rank granular sub-sections  
- **Multilingual Support**: Plug in language models for global document sets

---

## 📝 Credits

- Developed for the Adobe India Hackathon 2025 — "Connecting the Dots" Challenge  
- Built with Python, PyMuPDF, and a passion for smarter reading

---

## 📚 See Also

- [Approach Explanation](./approach_explanation.md) — In-depth methodology and design rationale
