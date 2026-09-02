import logging

from app.domain.use_cases.verifications.encryption_check import encryption_check
from app.domain.use_cases.verifications.file_only_has_images import file_has_only_images
from app.domain.use_cases.verifications.file_signature_validator import (
    validate_pdf_signature,
)
from app.domain.use_cases.verifications.liveness_check import liveness_check
from app.domain.use_cases.verifications.trailer_check import trailer_check

logger = logging.getLogger(__name__)

VALIDATORS = [
    ("File signature", validate_pdf_signature, True),
    ("Liveness", liveness_check, True),
    ("Trailer", trailer_check, True),
    ("Encryption", encryption_check, False),
    ("Image only", file_has_only_images, False),
]


def do_validation(document_content: bytes) -> bool:
    """Validates a document by running all registered checks.

    Args:
        document_content (bytes): The content of the document to be processed.
    Returns:
        bool: True if all verification steps pass, False otherwise.
    """
    for name, validator, expected in VALIDATORS:
        if validator(document_content) is not expected:
            logger.warning(f"{name} validation failed.")
            return False

    logger.info("All validation checks passed successfully.")
    return True
