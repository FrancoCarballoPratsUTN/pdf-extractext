import hashlib

from app.domain.exceptions.domain_exceptions import DocumentChecksumError


def generate_checksum(content: bytes) -> str:
    if not content:
        raise DocumentChecksumError("The content cannot be empty.")
    return hashlib.sha256(content).hexdigest()
