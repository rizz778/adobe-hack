# main.py

import os
import json
from pathlib import Path
from extractor import extract_outline

def process_pdfs():
    input_dir = Path("pdfs")
    output_dir = Path("outputs")
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_files = list(input_dir.glob("*.pdf"))
    
    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file.name}")
        try:
            result = extract_outline(str(pdf_file))
        except Exception as e:
            print(f"Failed to process {pdf_file.name}: {e}")
            continue

        output_file = output_dir / f"{pdf_file.stem}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        print(f"Saved: {output_file.name}")

if __name__ == "__main__":
    print("Starting PDF outline extraction...")
    process_pdfs()
    print("Done.")
