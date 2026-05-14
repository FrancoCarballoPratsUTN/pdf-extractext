from typing import Optional

class ProblemDetailError(Exception):
    """
    Base class for all domain exceptions.
    It follows the structure of RFC 9457.
    """
    def __init__(self, title: str, status: int, detail: str, type: str = "about:blank", instance: Optional[str] = None):
        self.title = title
        self.status = status
        self.detail = detail
        self.type = type
        self.instance = instance
        self.media_type = "application/problem+json" 
        super().__init__(self.detail)

class DocumentNotFoundError(ProblemDetailError):
    """Exception raised when a document is not found in the repository."""
    def __init__(self, detail: str = "The requested document does not exist."):
        super().__init__(title="Document Not Found", status=404, detail=detail, type="/errors/not-found")

class DocumentAlreadyExistsError(ProblemDetailError):
    """Exception raised when a document with the same checksum already exists."""
    def __init__(self, detail: str = "The document has already been processed previously."):
        super().__init__(title="Document Already Exists", status=409, detail=detail, type="/errors/already-exists")

class InvalidDocumentDataError(ProblemDetailError):
    """Exception raised when the provided document data is invalid."""
    def __init__(self, detail: str = "The document data is invalid or corrupted."):
        super().__init__(title="Invalid Document Data", status=400, detail=detail, type="/errors/invalid-data")

class DocumentProcessingError(ProblemDetailError):
    """Exception raised when there is an error processing a document."""
    def __init__(self, detail: str = "An unexpected error occurred while processing the file."):
        super().__init__(title="Document Processing Error", status=500, detail=detail, type="/errors/processing-failure")

class DocumentValidationError(ProblemDetailError):
    """Exception raised when there is an error validating a document."""
    def __init__(self, detail: str = "The document does not meet the validation requirements."):
        super().__init__(title="Document Validation Error", status=422, detail=detail, type="/errors/validation-error")

class DocumentConversionError(ProblemDetailError):
    """Exception raised when there is an error converting a document."""
    def __init__(self, detail: str = "The file could not be converted to the requested .txt format."):
        super().__init__(title="Document Conversion Error", status=500, detail=detail, type="/errors/conversion-error")

class DocumentChecksumError(ProblemDetailError):
    """Exception raised when there is an error with the document checksum."""
    def __init__(self, detail: str = "The integrity of the file could not be verified."):
        super().__init__(title="Document Checksum Error", status=400, detail=detail, type="/errors/checksum-mismatch")

class DocumentStorageError(ProblemDetailError):
    """Exception raised when there is an error with document storage."""
    def __init__(self, detail: str = "There was a problem saving the file."):
        super().__init__(title="Document Storage Error", status=500, detail=detail, type="/errors/storage-failure")
