from app.domain.interfaces.document_converter import Converter

class ProcessDocumentUseCase:
    """Use case for processing a document using a specified converter."""
    def __init__(self, converter: Converter):
        self.converter = converter  

    def execute(self, file_content: bytes, name:str):
        """
        Executes the document processing using the provided converter.
        Args:
                file_content (bytes): The content of the document to be processed.
                name (str): The name of the file being processed.
        Returns:
                bytes: The processed document content.
        """
        return self.converter.convert(file_content, name)