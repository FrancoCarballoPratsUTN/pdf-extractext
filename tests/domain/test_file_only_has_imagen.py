from app.domain.use_cases.verifications.file_only_has_imagen import file_has_imagen
from tests.domain.mock_pdf import create_mock_pdf


def test_file_has_imagen_true():
    """
    he PDF is only an image (scanned document).
    Expected: True, because no extractable text exists.
    """
    image_pdf = create_mock_pdf(encrypted=False, is_image=True)

    assert file_has_imagen(image_pdf) == True

def test_file_has_imagen_false():
    """
    The PDF has extractable text.
    Expected: False, because it's a digital text document, not just an image.
    """
    text_pdf = create_mock_pdf(encrypted=False)
    
    assert file_has_imagen(text_pdf) == False