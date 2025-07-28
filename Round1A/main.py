import os
import json
from utils.extractor import extract_outline

INPUT_DIR = os.path.join(os.path.dirname(__file__), 'input')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'output')

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith('.pdf'):
        pdf_path = os.path.join(INPUT_DIR, filename)
        outline = extract_outline(pdf_path)
        json_path = os.path.join(OUTPUT_DIR, os.path.splitext(filename)[0] + '.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(outline, f, ensure_ascii=False, indent=2) 