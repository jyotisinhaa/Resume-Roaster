"""
PDF / text extraction utilities for Resume Roaster.
"""

import fitz  # PyMuPDF


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extract all text from a PDF stored as bytes."""
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    text_parts: list[str] = []
    for page in doc:
        text_parts.append(page.get_text())
    doc.close()
    return "\n".join(text_parts).strip()


def extract_text(file_bytes: bytes, file_name: str) -> str:
    """
    Route to the correct parser based on file extension.
    Supports .pdf and .txt files.
    """
    name_lower = file_name.lower()
    if name_lower.endswith(".pdf"):
        return extract_text_from_pdf(file_bytes)
    elif name_lower.endswith(".txt"):
        return file_bytes.decode("utf-8", errors="replace").strip()
    else:
        raise ValueError(f"Unsupported file type: {file_name}")
