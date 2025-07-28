import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer, util
from datetime import datetime
from pathlib import Path
import json

# ----------------------
# Configurable Parameters
# ----------------------

INPUT_JSON = "collection1/1b_input.json"
PDF_DIR = Path("collection1/pdfs")  # Folder containing all PDFs
OUTPUT_JSON = "collection1/1b_output.json"
TOP_K = 5  # Top K sections per PDF

# ----------------------
# Utilities
# ----------------------

def extract_sections(filepath):
    doc = fitz.open(filepath)
    text_blocks = []
    for i, page in enumerate(doc):
        blocks = page.get_text("blocks")
        for block in blocks:
            text = block[4].strip()
            if len(text) > 30:
                text_blocks.append((i + 1, text))
    return text_blocks

def rank_relevant_sections(paragraphs, query_embedding, model, top_k=TOP_K):
    texts = [para[1] for para in paragraphs]
    para_embeddings = model.encode(texts, convert_to_tensor=True)
    scores = util.cos_sim(query_embedding, para_embeddings)[0]
    top_scores = scores.topk(k=top_k)
    ranked = [(texts[i], paragraphs[i][0], float(scores[i])) for i in top_scores.indices]
    return ranked  # [(text, page_number, score)]

# ----------------------
# Main Logic
# ----------------------

def main():
    with open(INPUT_JSON) as f:
        input_data = json.load(f)

    persona = input_data["persona"]["role"]
    job = input_data["job_to_be_done"]["task"]
    documents = input_data["documents"]

    model = SentenceTransformer("all-MiniLM-L6-v2")
    query = f"{persona}: {job}"
    query_embedding = model.encode(query, convert_to_tensor=True)

    extracted_sections = []
    subsection_analysis = []

    for doc in documents:
        filename = doc["filename"]
        pdf_path = PDF_DIR / filename

        if not pdf_path.exists():
            print(f"❌ Missing file: {filename}")
            continue

        print(f"🔍 Processing {filename}")
        paragraphs = extract_sections(pdf_path)
        if not paragraphs:
            print(f"⚠️ No text found in {filename}")
            continue

        ranked = rank_relevant_sections(paragraphs, query_embedding, model)

        for i, (text, page, _) in enumerate(ranked):
            extracted_sections.append({
                "document": filename,
                "section_title": text[:80],
                "page_number": page,
                "importance_rank": i + 1
            })
            subsection_analysis.append({
                "document": filename,
                "refined_text": text,
                "page_number": page
            })

    output = {
        "metadata": {
            "input_documents": [doc["filename"] for doc in documents],
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }

    with open(OUTPUT_JSON, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n✅ Output saved to {OUTPUT_JSON}")

if __name__ == "__main__":
    main()
