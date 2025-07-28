# 📘 Adobe India Hackathon 2025 – Challenge 1A: Understand Your Document

## 🔍 Overview

This repository contains the solution for **Round 1A** of the Adobe India Hackathon 2025 —  
_“Connecting the Dots Through Docs”._

The goal is to **automatically extract a structured outline** (Title, H1, H2, H3) from a set of PDF files and output them as clean JSON files.

---

## 🧠 Problem Statement

You're given unstructured PDF documents and need to make sense of their structure like a machine would. Your task is to:

- Extract the **Title**, **Headings (H1, H2, H3)** with associated **page numbers**
- Output this information in a predefined JSON format

---

## 📁 Directory Structure
```
1a/
├── maina.py # Main driver script to process all PDFs
├── extractor.py # Core logic for outline extraction
├── pdfs/ # Input folder containing .pdf files
└── outputs/ # Output folder containing generated .json files
```
---

## 🚀 How to Run

### 🐍 Prerequisites
```
- Python 3.7+
- Required Python libraries:
```
```bash
pip install pymupdf
```

### ▶️ Run the Script
```
cd 1a
python maina.py
```
This will:

Read all .pdf files in the pdfs/ folder

Extract structured outlines using extractor.py

Save the output JSON files to the outputs/ directory

## 📤 Sample Output Format
Each processed PDF will generate a corresponding .json file like this:
```
{
"title": "Understanding AI",
"outline": [
{ "level": "H1", "text": "Introduction", "page": 1 },
{ "level": "H2", "text": "What is AI?", "page": 2 },
{ "level": "H3", "text": "History of AI", "page": 3 }
]
}
```
## 🧰 Technologies Used
  PyMuPDF (fitz) — for PDF text and layout extraction
  
  Python Standard Libraries:
  
  os and pathlib — for file and directory handling
  
  json — for reading and writing structured output
  
  re — for optional regex matching (if used in extractor.py)
  
## ⚙️ Constraints Met

- ✅ **Input PDFs ≤ 50 pages** — Efficiently processes PDFs with up to 50 pages without performance degradation.
- ✅ **Title + Headings (H1, H2, H3)** — Extracts semantically significant headings and section content where applicable.
- ✅ **Output format (valid JSON)** — Produces well-structured, indented JSON output with required metadata and section info.
- ✅ **Execution time ≤ 10s/PDF** — Processes each PDF well within the 10-second constraint under typical system loads.
- ✅ **Offline-only (no API calls)** — All models and processing are local; no internet or API dependencies.
- ✅ **CPU-only execution (amd64)** — Fully compatible with CPU-only environments using amd64 architecture; no GPU required.
