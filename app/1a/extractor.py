# extractor.py

import fitz  # PyMuPDF

def extract_outline(pdf_path, max_heading_level=3):
    """
    Extracts the title and outline (headings) from a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.
        max_heading_level (int): The highest heading level to extract (e.g., 3 -> H1/H2/H3).

    Returns:
        dict: A dictionary with 'title' and 'outline' keys.
    """
    doc = fitz.open(pdf_path)
    candidates = []
    font_sizes = set()

    # Step 1: Parse all text spans, collect sizes and heading candidates
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if block["type"] != 0:  # skip images etc.
                continue
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    txt = span.get("text", "").strip()
                    if not txt:
                        continue
                    font_size = span["size"]
                    font_name = span["font"]
                    is_bold = "Bold" in font_name or "bold" in font_name
                    font_sizes.add(font_size)
                    # filter: only consider reasonable-length lines (not paragraphs)
                    if len(txt) <= 80:
                        candidates.append({
                            "text": txt,
                            "size": font_size,
                            "font": font_name,
                            "bold": is_bold,
                            "page": page_num + 1,
                            "y": span["bbox"][1],  # top y-coordinate
                            "block_no": block.get("number", 0),
                        })

    # Step 2: Title heuristics (largest font size on page 1, near the top)
    page1_candidates = [c for c in candidates if c["page"] == 1]
    if page1_candidates:
        max_size = max(c["size"] for c in page1_candidates)
        title_cands = [c for c in page1_candidates if c["size"] == max_size]
        # pick the one closest to 'top' of page
        title = min(title_cands, key=lambda x: x["y"])["text"]
    else:
        title = ""

    # Step 3: Heading level mapping (largest N unique sizes for H1..HN)
    font_sizes_sorted = sorted(font_sizes, reverse=True)
    heading_sizes = font_sizes_sorted[:max_heading_level]
    level_names = ["H{}".format(i+1) for i in range(max_heading_level)]
    size2level = {sz: lvl for sz, lvl in zip(heading_sizes, level_names)}

    # Optional: If many close sizes, you may want to cluster/group fonts.

    # Step 4: Assign levels
    outline = []
    for c in candidates:
        lvl = size2level.get(c["size"])
        if lvl:
            outline.append({
                "level": lvl,
                "text": c["text"],
                "page": c["page"]
            })

    # Optional: remove duplicates (e.g., running headers/footers)

    return {"title": title, "outline": outline}
