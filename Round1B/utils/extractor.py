import fitz  # PyMuPDF
import re

def extract_sections(pdf_path):
    doc = fitz.open(pdf_path)
    sections = []
    heading_patterns = [
        re.compile(r'^[A-Z][A-Z\s\d\-:,.]{3,}$'),  # ALL CAPS headings
        re.compile(r'^(\d+\.?)+\s+.+'),            # Numbered headings (e.g., 1. Introduction)
    ]
    font_sizes = {}
    # Pass 1: Collect font sizes to estimate heading levels
    for page in doc:
        blocks = page.get_text('dict')['blocks']
        for block in blocks:
            for line in block.get('lines', []):
                for span in line.get('spans', []):
                    size = span['size']
                    font_sizes[size] = font_sizes.get(size, 0) + 1
    # Heuristic: Largest font = H1, next = H2, next = H3
    sorted_sizes = sorted(font_sizes.items(), key=lambda x: -x[0])
    size_to_level = {}
    for i, (size, _) in enumerate(sorted_sizes[:3]):
        size_to_level[size] = f'H{i+1}'
    # Pass 2: Extract headings and their text
    for page_num, page in enumerate(doc, 1):
        blocks = page.get_text('dict')['blocks']
        for block in blocks:
            for line in block.get('lines', []):
                for span in line.get('spans', []):
                    text = span['text'].strip()
                    if not text:
                        continue
                    size = span['size']
                    level = size_to_level.get(size)
                    # Also check heading patterns
                    is_heading = False
                    for pat in heading_patterns:
                        if pat.match(text):
                            is_heading = True
                            break
                    if level or is_heading:
                        sections.append({
                            'section_title': text,
                            'level': level if level else 'H3',
                            'page': page_num,
                            'text': text  # For now, just the heading; can expand to section text
                        })
    # Optionally, group text under headings (not implemented here for brevity)
    return sections 