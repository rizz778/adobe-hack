# 📄 Adobe India Hackathon 2025 – Challenge 1B: Persona-Driven Document Intelligence

## 🔍 Overview

This repository contains a solution for **Round 1B** of the Adobe India Hackathon 2025 — _"Connect What Matters — For the User Who Matters."_  
The goal is to **intelligently extract and rank the most relevant sections** from a set of input PDFs based on a **persona** and a **job-to-be-done**.

---

## 🧠 Problem Statement

Given:

- A **persona** (role with specific focus)
- A **job-to-be-done** (task the persona is trying to accomplish)
- A **collection of related PDFs**

You are to:

- Understand the documents from a semantic perspective
- Extract the **top-K most relevant sections**
- Rank them by relevance
- Output both a high-level and a granular analysis of the retrieved sections

---

## 📁 Directory Structure

1b/
├── collection1/
│ ├── pdfs/ # Folder containing input PDF files
│ ├── 1b_input.json # JSON input with persona, job, and filenames
│ └── 1b_output.json # Output with ranked sections and refined text
├── collection2/
│ ├── mainb.py # Python script for processing documents
│ └── readme.md # This README file

---

## 🚀 How It Works

### Step-by-Step

1. **Input**: The system accepts a JSON file (`1b_input.json`) containing:

   - A persona description
   - A job-to-be-done
   - A list of PDFs to analyze

2. **Embedding**: The query (persona + job) and document sections are encoded using a transformer (`all-MiniLM-L6-v2`).

3. **Text Extraction**: The script uses PyMuPDF (`fitz`) to extract meaningful blocks of text from each page.

4. **Relevance Ranking**: Cosine similarity is computed between the query and all extracted sections. The top-K most relevant sections are selected per document.

5. **Output Generation**: The script generates an output JSON file with:
   - `metadata` (documents used, persona, job, timestamp)
   - `extracted_sections` (top-K section titles and pages)
   - `subsection_analysis` (refined content per section)

---

## 🧰 Technologies Used

- [**PyMuPDF** (`fitz`)](https://pymupdf.readthedocs.io/) — Used for parsing and extracting text blocks from PDF files.
- [**Sentence-Transformers**](https://www.sbert.net/) — Used to generate semantic embeddings for persona+job queries and document text using `all-MiniLM-L6-v2`.
- **Python Standard Libraries**:
  - `json` — for reading and writing structured input/output.
  - `datetime` — to log processing timestamps.
  - `pathlib` — for cross-platform path management.
