from app.domain.use_cases.flows.flow_validation import do_validation
from app.domain.use_cases.flows.flow_building import flow_building
from app.domain.entities.document import Document
from app.infrastructure.converters.extract_text import ExtractText
class ProcessDocumentUseCase:
    """Use case for processing a document using a specified converter."""
    def __init__(self):
        self.converter = ExtractText()  

    def execute(self, file_content: bytes, filename: str)-> Document:
        """
        Executes the document processing using the provided converter.
        Args:
                file_content (bytes): The content of the document to be processed.
                filename (str): The name of the document file.
        Returns:
                Document: The processed document entity.
        """
        if not do_validation(file_content): 
            raise ValueError("Invalid PDF or corrupted file.")

        text = self.converter.convert(file_content)
        text_encode = text.encode('utf-8')
        return flow_building(text_encode, filename)