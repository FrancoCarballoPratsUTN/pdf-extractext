import io
import base64
from io import BytesIO
from docling.document_converter import PdfFormatOption
from docling.datamodel.base_models import InputFormat
from app.domain.interfaces.document_converter import Converter
from docling.datamodel.base_models import DocumentStream
from docling.document_converter import DocumentConverter
from docling.datamodel.pipeline_options import PdfPipelineOptions


class DoclingConverterMd(Converter):
    def convert(self, content: bytes, name: str) -> str:
        """Converts PDF content to Markdown format using the Docling library.
        Args:
                content (bytes): The content of the PDF document to be converted.
                name (str): The name of the PDF document, used for identification.
        Returns:
                str: The converted Markdown content as a string.
                """
        buf = io.BytesIO(content)
        source = DocumentStream(name= name, stream=buf)
        
        pipeline_options = PdfPipelineOptions()
        pipeline_options.do_ocr = False                
        pipeline_options.do_table_structure = True      
        pipeline_options.generate_page_images = True
        pipeline_options.images_scale = 2.0   

        converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
                }
            )
        result = converter.convert(source)
        markdown_output = result.document.export_to_markdown(image_mode="embedded")
        
        return markdown_output
