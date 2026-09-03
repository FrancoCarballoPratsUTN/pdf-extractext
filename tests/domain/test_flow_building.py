from datetime import UTC, datetime

from app.domain.entities.document import Document
from app.domain.use_cases.checksum import generate_checksum
from app.domain.use_cases.flows.flow_building import flow_building


def test_flow_building_creates_document():
    text = "Hello world"
    filename = "test.pdf"

    before = datetime.now(UTC)
    doc = flow_building(text, filename)
    after = datetime.now(UTC)

    # Verifica que sea la entidad correcta
    assert isinstance(doc, Document)
    assert doc.text == text
    assert doc.file_name == filename

    # Verifica que el checksum se calculó bien con la función real
    assert doc.checksum == generate_checksum(text.encode("utf-8"))

    # Verifica que la fecha se generó en el momento
    assert before <= doc.date <= after
