from app.domain.use_cases.verifications.encryption_check import encryption_check
from tests.domain.mock_pdf import create_mock_pdf


def test_encryption_check_encrypted():
    """Test that the encryption_check function returns True for an encrypted PDF."""
    encrypted_pdf = create_mock_pdf(encrypted=True)
    assert encryption_check(encrypted_pdf)


def test_encryption_check_not_encrypted():
    """Test that the encryption_check function returns False for a non-encrypted PDF."""
    not_encrypted_pdf = create_mock_pdf(encrypted=False)
    assert not encryption_check(not_encrypted_pdf)
