import logging

from app.domain.contracts.document_converter import Converter
from app.domain.use_cases.verifications.open_pdf import open_pdf

logger = logging.getLogger(__name__)


class ExtractText(Converter):
    def convert(self, file_content: bytes) -> str:
        """Extracts text from a PDF file.
        Args:
            file_content (bytes): The content of the PDF file as bytes.
        Returns:
            str: The extracted text from the PDF file."""
        try:
            reader = open_pdf(file_content)
            text = "\n".join([page.extract_text() for page in reader.pages])

            logger.info("Text extracted from PDF successfully.")
            return text
        except Exception as e:
            logger.critical("Error extracting text from PDF", exc_info=True)
            raise e
