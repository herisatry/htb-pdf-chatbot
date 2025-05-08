import os
from app.loaders import extract_text_from_pdfs, chunk_text

def test_extract_text_from_sample_pdf(tmp_path):
    sample_path = tmp_path / "test.pdf"
    sample_path.write_text("Dummy PDF content")
    result = extract_text_from_pdfs(str(tmp_path))
    assert isinstance(result, str)

def test_chunk_text():
    text = "A" * 5000
    chunks = chunk_text(text, chunk_size=1000, chunk_overlap=100)
    assert len(chunks) > 1
    assert all(isinstance(chunk, str) for chunk in chunks)
