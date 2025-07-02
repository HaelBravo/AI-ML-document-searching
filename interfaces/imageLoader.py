import io
from PIL import Image

from my_app.interfaces.baseLoader import BaseLoader


class ImageLoader(BaseLoader):
    
    def load(self, bytesString: bytes) -> list[Image.Image]:
        # Wrap bytes into a file-like object:
        image_stream = io.BytesIO(bytesString)
        # Open Image with pillow:
        img = Image.open(image_stream)
        return [img]
