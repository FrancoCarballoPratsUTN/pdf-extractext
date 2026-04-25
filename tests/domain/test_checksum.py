from app.domain.exceptions.domain_exceptions import DocumentChecksumError
import pytest
from app.domain.use_cases.checksum import generate_checksum


def test_same_document_generates_same_checksum():
    pdf = b"%PDF- fake content"
    c1 = generate_checksum(pdf)
    c2 = generate_checksum(pdf)
    assert c1 == c2

def test_different_documents_generate_different_checksums():
    pdf1 = b"%PDF file one"
    pdf2 = b"%PDF file two"
    c1 = generate_checksum(pdf1)
    c2 = generate_checksum(pdf2)
    assert c1 != c2

def test_empty_document_raises_error():
    with pytest.raises(DocumentChecksumError):
        generate_checksum(b"")