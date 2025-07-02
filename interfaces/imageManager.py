# import cv2
# import numpy as np
from PIL import Image, ImageOps, ImageFilter
import pytesseract

from my_app.interfaces.baseImageManager import BaseImageManager


class ImageManager(BaseImageManager):

    def preprocess_image(self, pil_image: Image.Image) -> Image.Image:
        #TODO: Manage the type of file images

        # Convert PIL image to OpenCV format
        # img = np.array(pil_image)
        # img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)       # Grayscale
        # img = cv2.GaussianBlur(img, (3, 3), 0)            # Denoise
        # _, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)  # Binarize
        # Convert to grayscale
        image = pil_image.convert("L")
        # Apply autocontrast
        image = ImageOps.autocontrast(image)
        # Optional: apply sharpening
        image = image.filter(ImageFilter.SHARPEN)

        # Convert back to PIL
        return image

    def extract_text_from_image(self, image: Image.Image) -> str:
        text = pytesseract.image_to_string(image)
        return text

