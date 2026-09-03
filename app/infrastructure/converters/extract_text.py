import logging

from app.domain.contracts.document_converter import Converter
from app.domain.exceptions.domain_exceptions import DocumentConversionError
from app.domain.use_cases.verifications.open_pdf import open_pdf

logger = logging.getLogger(__name__)


class ExtractText(Converter):
    def convert(self, file_content: bytes) -> str:
        """Extracts text from a PDF file byte stream.

        Args:
            file_content (bytes): The binary content of the PDF.

        Returns:
            str: Extracted text joined by newlines.

        Raises:
            DocumentConversionError: If parsing or extraction fails.
        """
        try:
            reader = open_pdf(file_content)
            extracted_pages = [page.extract_text() or "" for page in reader.pages]
            text = "\n".join(extracted_pages)

            logger.info("Text extracted from PDF successfully.")
            return text

        except Exception as error:
            logger.error("Failed to extract text from PDF: %s", error, exc_info=True)
            raise DocumentConversionError("Error converting PDF to text") from error

