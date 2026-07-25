from io import BytesIO
from pypdf import PdfReader
from app.domain.contracts.document_converter import Converter
from app.config.logging_config import loger


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
            
            loger.info("Text extracted from PDF successfully.")
            return text
        except Exception as e:
            loger.critical("Error extracting text from PDF", exc_info=True)
            