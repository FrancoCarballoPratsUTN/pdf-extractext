import hashlib

def generate_checksum(content: bytes) -> str:
    if not content:
        raise ValueError("The content cannot be empty.")
    return hashlib.sha256(content).hexdigest()