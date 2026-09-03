import pytest

from app.domain.exceptions.domain_exceptions import DocumentConversionError
from app.infrastructure.converters.extract_text import ExtractText
from tests.domain.mock_pdf import create_mock_pdf


@pytest.fixture
def converter():
    return ExtractText()

def test_invalid_pdf_conversion_raises_domain_error(converter):
    invalid_pdf_content = b"%PDF-1.4\n%...\n"

    with pytest.raises(DocumentConversionError):
        converter.convert(invalid_pdf_content)

def test_extract_text_conversion_returns_expected_content(converter):
    pdf_content = create_mock_pdf(encrypted=False)
    text_result = converter.convert(pdf_content)
    assert bool(text_result.strip()) is True
