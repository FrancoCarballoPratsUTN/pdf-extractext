import pytest
from tests.domain.mock_pdf import create_mock_pdf
from app.domain.use_cases.verifications.liveness_check import liveness_check

@pytest.fixture
def invalid_liveness_data():
    """Fixture that provides invalid liveness check data for testing, without Xref table."""
    return b"%PDF-1.4\n%...\n"

@pytest.fixture
def valid_liveness_data():
    """Fixture that provides valid liveness check data for testing."""
    return create_mock_pdf(encrypted=False)

def test_liveness_check_valid(valid_liveness_data):
    """Test that the liveness_check function returns True for valid PDF content."""
    assert liveness_check(valid_liveness_data) == True

def test_liveness_check_invalid(invalid_liveness_data):
    """Test that the liveness_check function returns False for invalid PDF content."""
    assert liveness_check(invalid_liveness_data) == False