# Approach Explanation: Persona-Driven Document Intelligence (Round 1B)

## 🧾 Overview

This solution transforms static PDF collections into intelligent, persona-aware knowledge resources.  
By extracting, ranking, and surfacing the most relevant sections for a given persona and job-to-be-done, it enables context-driven document exploration and insight generation.

---

## 🧠 Methodology

1. **Input Handling**  
   - Each test case folder contains an `input.json` specifying the persona, job-to-be-done, and a list of PDF file paths.  
   - The system processes all test case folders in one run, generating outputs in their respective directories.

2. **PDF Section Extraction**  
   - Utilizes `PyMuPDF (fitz)` to parse each PDF, extracting headings (H1, H2, H3) and their page numbers using font size analysis and heading pattern recognition.  
   - Each section is represented with its title, level, page, and text snippet, providing a structured view of the document's hierarchy.

3. **Persona & Job Understanding**  
   - The persona and job-to-be-done are parsed from `input.json`.  
   - Keywords are extracted from both persona focus areas and job description, forming a relevance profile for the user’s intent.

4. **Relevance Ranking**  
   - Each section is scored based on keyword overlap with the persona/job profile.  
   - Sections are ranked by relevance, with ties broken by document order, and assigned an `importance_rank`.  
   - This ensures the most contextually important sections are surfaced first for the user’s needs.

5. **Output Generation**  
   - For each test case, an `output.json` is written to the same folder, containing:
     - Metadata (input docs, persona, job, timestamp)  
     - Ranked extracted sections  
     - *(Extensible)* Sub-section analysis for deeper insights

---

## ⚙️ Design Choices

- **Generality**: No file-specific logic or hardcoded keywords; the system generalizes across academic, business, and educational domains.  
- **Performance**: Efficient parsing and ranking ensure all documents are processed within the required time constraints (≤ 60s for 3–5 PDFs).  
- **Offline & Secure**: All processing is local, with no network calls or external dependencies, ensuring privacy and compliance.  
- **Modularity**: The codebase is organized for easy extension—future improvements (e.g., semantic similarity, multilingual support, advanced NLP) can be integrated with minimal changes.

---

## ✅ Compliance with Challenge Requirements

- **Input / Output**: Accepts persona, job, and PDFs via `input.json`; outputs are written per test case folder  
- **Dockerization**: The Dockerfile ensures compatibility with AMD64 architecture and CPU-only execution  
- **No Network Dependency**: Solution runs fully offline  
- **Model Size**: All dependencies are lightweight and within the 1GB limit

---

## 🔮 Extensibility & Future Directions

- **Semantic Relevance**: The ranking logic can be enhanced with semantic similarity (e.g., spaCy, transformer models) for deeper understanding  
- **Sub-section Analysis**: The framework supports granular extraction and ranking of sub-sections for even more targeted insights  
- **Multilingual Support**: The modular design allows for easy integration of multilingual NLP pipelines

---

## 🏁 Conclusion

This approach delivers a **robust**, **extensible**, and **context-aware** document intelligence system.  
It bridges the gap between static content and user-centric knowledge, laying the foundation for next-generation document experiences.
