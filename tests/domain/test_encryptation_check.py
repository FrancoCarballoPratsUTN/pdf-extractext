from app.domain.use_cases.verifications.encryptation_check import encryptation_check
from tests.domain.mock_pdf  import create_mock_pdf


def test_encryptation_check_encrypted():
    """Test that the encryptation_check function returns True for an encrypted PDF."""
    encrypted_pdf = create_mock_pdf(encrypted=True)
    assert encryptation_check(encrypted_pdf) == True

def test_encryptation_check_not_encrypted():
    """Test that the encryptation_check function returns False for a non-encrypted PDF."""
    not_encrypted_pdf = create_mock_pdf(encrypted=False)
    assert encryptation_check(not_encrypted_pdf) == False

