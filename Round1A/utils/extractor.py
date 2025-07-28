import fitz  # PyMuPDF
import re
from collections import Counter

def is_heading(text, font_size, h1_size, h2_size, h3_size, flags):
    # Heuristic: heading if matches one of the main heading sizes or is bold/all-caps/numbered
    if font_size in (h1_size, h2_size, h3_size):
        return True
    if flags & 2:  # bold
        if len(text) < 80 and text.isupper():
            return True
    if re.match(r'^(\d+\.|[A-Z]\.|[IVX]+\.)', text):
        return True
    return False

def get_level(font_size, h1_size, h2_size, h3_size):
    if font_size == h1_size:
        return 'H1'
    elif font_size == h2_size:
        return 'H2'
    elif font_size == h3_size:
        return 'H3'
    return None

def extract_outline(pdf_path):
    """
    Extracts the document title and outline (H1, H2, H3 headings with page numbers) from the given PDF.
    Returns a dict with 'title' and 'outline' keys.
    """
    doc = fitz.open(pdf_path)
    font_sizes = []
    blocks_per_page = []
    all_blocks = []

    # Step 1: Extract all text blocks with font info
    for page_num, page in enumerate(doc, 1):
        blocks = []
        for b in page.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                for s in l.get("spans", []):
                    text = s["text"].strip()
                    if not text:
                        continue
                    font_size = s["size"]
                    font_name = s["font"]
                    flags = s["flags"]
                    block = {
                        "text": text,
                        "font_size": font_size,
                        "font_name": font_name,
                        "flags": flags,
                        "bbox": s["bbox"],
                        "page": page_num
                    }
                    blocks.append(block)
                    all_blocks.append(block)
                    font_sizes.append(font_size)
        blocks_per_page.append(blocks)

    # Step 2: Title = largest font on page 1
    if blocks_per_page and blocks_per_page[0]:
        title_block = max(blocks_per_page[0], key=lambda b: b["font_size"])
        title = title_block["text"]
        title_size = title_block["font_size"]
    else:
        title = ""
        title_size = None

    # Step 3: Heading detection
    # Exclude title size from heading candidates
    font_counter = Counter([fs for fs in font_sizes if fs != title_size])
    most_common = font_counter.most_common()
    if not most_common:
        return {"title": title, "outline": []}
    h1_size = most_common[0][0]
    h2_size = most_common[1][0] if len(most_common) > 1 else None
    h3_size = most_common[2][0] if len(most_common) > 2 else None

    outline = []
    for block in all_blocks:
        text = block["text"]
        font_size = block["font_size"]
        flags = block["flags"]
        page = block["page"]
        if font_size == title_size and text == title:
            continue  # skip title
        if is_heading(text, font_size, h1_size, h2_size, h3_size, flags):
            level = get_level(font_size, h1_size, h2_size, h3_size)
            if not level:
                # fallback: bold/all-caps/numbered
                if flags & 2 and text.isupper():
                    level = 'H3'
                elif re.match(r'^(\d+\.|[A-Z]\.|[IVX]+\.)', text):
                    level = 'H3'
                else:
                    continue
            outline.append({
                "level": level,
                "text": text,
                "page": page
            })

    return {
        "title": title,
        "outline": outline
    } 