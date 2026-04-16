from app.infrastructure.converters.extract_text import ExtractText
from tests.domain.mock_pdf import create_mock_pdf
import pytest

def test_invalid_pdf_conversion():
    """Test the conversion of an invalid PDF file using the ExtractText converter."""
    invalid_pdf_content = b"%PDF-1.4\n%...\n"  
    converter = ExtractText()
    with pytest.raises(Exception):
        converter.convert(invalid_pdf_content)


def test_extract_text_conversion():
    """Test the conversion of a PDF to text using the ExtractText converter."""
    pdf_content = create_mock_pdf(encrypted= False)
    converter = ExtractText()
    text_result = converter.convert(pdf_content)

    assert text_result.strip() != "", "The converted text should not be empty."


