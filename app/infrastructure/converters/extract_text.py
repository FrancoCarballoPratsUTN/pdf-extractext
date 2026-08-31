import logging
from io import BytesIO

from pypdf import PdfReader

from app.domain.contracts.document_converter import Converter

logger = logging.getLogger(__name__)


class ExtractText(Converter):
    def convert(self, file_content: bytes) -> str:
        """Extracts text from a PDF file.
        Args:
            file_content (bytes): The content of the PDF file as bytes.
        Returns:
            str: The extracted text from the PDF file."""
        try:
            file_bytes = BytesIO(file_content)
            reader = PdfReader(file_bytes)
            text = "\n".join([pagina.extract_text() for pagina in reader.pages])

            logger.info("Text extracted from PDF successfully.")
            return text
        except Exception as e:
            logger.critical("Error extracting text from PDF", exc_info=True)
            raise e
