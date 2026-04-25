class DocumentNotFoundError(Exception):
    """Exception raised when a document is not found in the repository."""
    pass
class DocumentAlreadyExistsError(Exception):
    """Exception raised when a document with the same checksum already exists in the repository."""
    pass
class InvalidDocumentDataError(Exception):
    """Exception raised when the provided document data is invalid."""
    pass
class DocumentProcessingError(Exception):
    """Exception raised when there is an error processing a document."""
    pass
class DocumentValidationError(Exception):
    """Exception raised when there is an error validating a document."""
    pass
class DocumentConversionError(Exception):
    """Exception raised when there is an error converting a document."""
    pass
class DocumentChecksumError(Exception):
    """Exception raised when there is an error with the document checksum."""
    pass
class DocumentStorageError(Exception):
    """Exception raised when there is an error with document storage."""
    pass
