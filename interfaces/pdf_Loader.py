from pdf2image import convert_from_bytes
from PIL import Image

from my_app.interfaces.baseLoader import BaseLoader


class PDFLoader(BaseLoader):
    def __init__(self):
        pass

    def load(self, file_bytes: bytes) -> list[Image.Image]:
        """Convert PDF bytes into a list of PIL images (one per page)."""
        images = convert_from_bytes(file_bytes)
        return images