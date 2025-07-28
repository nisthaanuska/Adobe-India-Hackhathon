import os
import json
from utils.extractor import extract_sections
from utils.relevance import rank_sections
from datetime import datetime

# Set up base directory relative to this script
BASE_DIR = os.path.dirname(__file__)

# Find all test case folders (each containing input.json)
test_case_folders = [
    d for d in os.listdir(BASE_DIR)
    if os.path.isdir(os.path.join(BASE_DIR, d)) and os.path.exists(os.path.join(BASE_DIR, d, 'input.json'))
]

if not test_case_folders:
    raise FileNotFoundError('No test case folder with input.json found.')

for test_case in test_case_folders:
    TEST_CASE_DIR = os.path.join(BASE_DIR, test_case)
    print(f'Processing test case: {test_case}')
    # Load input.json
    with open(os.path.join(TEST_CASE_DIR, 'input.json'), 'r', encoding='utf-8') as f:
        input_data = json.load(f)
    persona = input_data['persona']
    job = input_data['job_to_be_done']
    document_paths = input_data['documents']

    all_sections = []
    pdf_files = []
    for rel_pdf_path in document_paths:
        pdf_path = os.path.join(TEST_CASE_DIR, rel_pdf_path)
        pdf_files.append(os.path.relpath(pdf_path, BASE_DIR))
        sections = extract_sections(pdf_path)
        ranked = rank_sections(sections, persona, job)
        for r in ranked:
            r['document'] = os.path.relpath(pdf_path, BASE_DIR)
        all_sections.extend(ranked)

    # Prepare output JSON
    output = {
        'metadata': {
            'input_documents': pdf_files,
            'persona': persona,
            'job_to_be_done': job,
            'processing_timestamp': datetime.utcnow().isoformat() + 'Z'
        },
        'extracted_sections': all_sections,
        # 'subsection_analysis': ... # To be implemented
    }

    # Write output.json to the test case folder
    with open(os.path.join(TEST_CASE_DIR, 'output.json'), 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f'Output written to {os.path.join(TEST_CASE_DIR, "output.json")}') 