from app.domain.interfaces.document_converter import Converter

class SaveDocumentUseCase:

    def __init__(self, converter: Converter):
        pass
    
    def execute(self, file_content: bytes):
        pass