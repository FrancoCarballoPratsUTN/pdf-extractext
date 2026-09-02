from app.domain.use_cases.verifications.file_only_has_images import file_has_only_images
from tests.domain.mock_pdf import create_mock_pdf


def test_file_has_only_images_true():
    """
    The PDF is only an image (scanned document).
    Expected: True, because no extractable text exists.
    """
    image_pdf = create_mock_pdf(encrypted=False, is_image=True)

    assert file_has_only_images(image_pdf)


def test_file_has_only_images_false():
    """
    The PDF has extractable text.
    Expected: False, because it's a digital text document, not just an image.
    """
    text_pdf = create_mock_pdf(encrypted=False)

    assert not file_has_only_images(text_pdf)
