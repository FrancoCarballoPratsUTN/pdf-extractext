from app.domain.use_cases.verifications.file_only_has_imagen import file_has_imagen
from app.domain.use_cases.verifications.encryptation_check import encryptation_check
from app.domain.use_cases.verifications.file_signature_validator import validate_pdf_signature
from app.domain.use_cases.verifications.liveness_check import liveness_check  
from app.domain.use_cases.verifications.trailer_check import trailer_check

def do_validation(document_content: bytes)-> bool:
    """Executes the document processing pipeline, which includes various verification steps.
    Args:
        document_content (bytes): The content of the document to be processed.
    Returns:
        bool: True if all verification steps pass, False otherwise.
    """
    if not validate_pdf_signature(document_content):
        print("File signature validation failed.")
        return False
    if not liveness_check(document_content):
        print("Liveness check failed.")
        return False
    if not trailer_check(document_content):
        print("Trailer check failed.")
        return False
    if encryptation_check(document_content):
        print("Encryptation check failed.")
        return False
    if not file_has_imagen(document_content):
        print("File only has image check failed.")
        return False
    return True