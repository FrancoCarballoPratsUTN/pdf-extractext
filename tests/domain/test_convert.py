from app.infrastructure.converters.docling_md import DoclingConverterMd
from tests.domain.mock_pdf import create_mock_pdf
from docling.exceptions import ConversionError 
import pytest

def test_invalid_pdf_conversion():
    """Test the conversion of an invalid PDF to Markdown using the DoclingConverter."""
    invalid_pdf_content = b"%PDF-1.4\n%...\n"  
    converter = DoclingConverterMd()

    with pytest.raises(ConversionError):
        converter.convert(invalid_pdf_content, name="invalid_sample.pdf")


def test_docling_conversion():
    """Test the conversion of a PDF to Markdown using the DoclingConverter."""
    pdf_content = create_mock_pdf(encrypted= False)
    converter = DoclingConverterMd()
    markdown_result = converter.convert(pdf_content, name="sample.pdf")

    assert markdown_result.strip() != "", "The converted Markdown should not be empty."


