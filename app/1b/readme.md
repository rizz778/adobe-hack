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

```
1b/
├── collection1/
│   ├── pdfs/                # Folder containing input PDF files
│   ├── 1b_input.json        # JSON input with persona, job, and filenames
│   └── 1b_output.json       # Output with ranked sections and refined text
├── mainb.py             # Python script for processing documents
|── readme.md            # This README file
```


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
## 🛠️ How to Run

### 1. 🔧 Install Dependencies

Make sure you have Python 3.8+ installed. Then run:

```bash
pip install -r requirements.txt
```
### 2. 📂 Place Files
Place all input PDF files in: 1b/collection1/pdfs/

Create the input JSON: 1b/collection1/1b_input.json

Example 1b_input.json format:
```
{
  "persona": { "role": "UX Designer" },
  "job_to_be_done": { "task": "Redesign user onboarding flow" },
  "documents": [
    { "filename": "doc1.pdf" },
    { "filename": "doc2.pdf" }
  ]
}
```


## 🐳 Docker Instructions

### 1. Build the Docker Image

```sh
docker build --platform linux/amd64 -t adobe-hack-1b:v1 .
```

### 2. Run the Docker Container

```sh
docker run --rm -v $(pwd)/collection1/pdfs:/app/collection1/pdfs -v $(pwd)/collection1:/app/collection1 --network none adobe-hack-1b:v1
```

- Place your PDFs in `collection1/pdfs/`
- Place your `1b_input.json` in `collection1/`
- The output `1b_output.json` will be generated in `collection1/
### 3. ▶️ Run the Script
Navigate to the root directory of the project (1b/) and run:
```
python mainb.py
```
---
## 🧰 Technologies Used

- [**PyMuPDF** (`fitz`)](https://pymupdf.readthedocs.io/) — Used for parsing and extracting text blocks from PDF files.
- [**Sentence-Transformers**](https://www.sbert.net/) — Used to generate semantic embeddings for persona+job queries and document text using `all-MiniLM-L6-v2`.
- **Python Standard Libraries**:
  - `json` — for reading and writing structured input/output.
  - `datetime` — to log processing timestamps.
  - `pathlib` — for cross-platform path management.

 ---
 ## ✅ Constraints Met

- ✅ **Multi-PDF Support**: Handles multiple documents in a single run as specified in the input JSON.
- ✅ **Persona + Job-To-Be-Done Conditioning**: Embeddings are generated using a natural language query formed from both persona and job-to-be-done context.
- ✅ **Semantic Understanding**: Utilizes a transformer model (`all-MiniLM-L6-v2`) to compute semantic relevance between input query and document content.
- ✅ **Granular Section Analysis**: Extracts meaningful paragraph-level text blocks (min length > 30 chars) from PDFs.
- ✅ **Top-K Section Ranking**: Ranks and selects top-K most relevant sections per document based on cosine similarity scores.
- ✅ **Structured Output**: Outputs a JSON file containing:
  - `metadata` (persona, job, documents used, timestamp)
  - `extracted_sections` (ranked highlights)
  - `subsection_analysis` (detailed content)
- ✅ **Robust Text Extraction**: Uses PyMuPDF to extract structured text blocks from all pages of the PDF.
- ✅ **Error Handling**: Skips missing PDFs and warns about empty documents without crashing.
- ✅ **Portable Paths**: Uses `pathlib` for platform-independent file handling.
- ✅ **Lightweight & Efficient**: Runs with a lightweight transformer model suitable for local or cloud environments.


