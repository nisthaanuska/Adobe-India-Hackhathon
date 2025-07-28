# Approach Explanation: PDF Outline Extractor(Round 1A)

## Overview
This solution is designed to extract a structured outline from PDF documents, including the document title and hierarchical headings(H1, H2, H3) with their corresponding page numbers.The extracted outline enables smarter document navigation, semantic search, and downstream document intelligence tasks.

## Methodology
1. ** PDF Parsing **: Utilizes PyMuPDF(fitz) to parse PDF files and extract text, font sizes, and layout information from each page.
2. ** Heading Detection **:
   - ** Font Size Heuristics **: The solution analyzes font sizes across the document to identify the largest(H1), second largest(H2), and third largest(H3) text spans, which typically correspond to headings.
   - ** Pattern Matching **: Additional regular expressions are used to detect common heading patterns(e.g., numbered headings, ALL CAPS headings) to improve robustness across diverse document styles.
3. ** Outline Construction **: For each detected heading, the solution records:
- The heading level(H1, H2, H3)
    - The heading text
        - The page number where the heading appears
4. ** Output Formatting **: The extracted outline is structured as a JSON object, with the document title and an array of outline entries, each specifying the heading level, text, and page number.

## Design Choices
    - ** No Hardcoding **: The solution does not rely on file - specific logic or hardcoded heading lists, ensuring generalizability across different PDFs.
- ** Performance **: The extraction process is optimized for speed, processing a 50 - page PDF in under 10 seconds on standard hardware.
- ** Offline Operation **: All processing is performed locally, with no internet or external API calls, meeting the offline execution requirement.
- ** Modularity **: The codebase is organized into modular components(main script, extractor utility) to facilitate reuse and extension in future rounds.

## Compliance with Challenge Requirements
    - ** Input / Output **: Accepts PDFs from `/app/input/` and writes JSON outputs to`/app/output/`.
- ** Dockerization **: The provided Dockerfile ensures compatibility with AMD64 architecture and CPU - only execution.
- ** No Network Dependency **: The solution runs entirely offline.
- ** Model Size **: No large models are used; dependencies are lightweight.

## Extensibility
    - The modular design allows for easy integration of more advanced NLP techniques(e.g., spaCy) for improved heading detection or multilingual support in future iterations.

## Conclusion
This approach provides a robust, efficient, and extensible foundation for document structure extraction, serving as the "brains" for more advanced document intelligence tasks in subsequent challenge rounds. 