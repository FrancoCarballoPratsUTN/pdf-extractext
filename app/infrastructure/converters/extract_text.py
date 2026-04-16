
from app.domain.interfaces.document_converter import Converter
from pypdf import PdfReader
from io import BytesIO

class ExtractText(Converter):
    def convert(self, file_content: bytes) -> str:
        """Extracts text from a PDF file.
            Args:
                file_content (bytes): The content of the PDF file as bytes.
            Returns:
                str: The extracted text from the PDF file."""
        file_bytes = BytesIO(file_content)
        reader = PdfReader(file_bytes)
        text = "\n".join([pagina.extract_text() for pagina in reader.pages])  

        return text