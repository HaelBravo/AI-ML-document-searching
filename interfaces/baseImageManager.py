from abc import ABC, abstractmethod
# import cv2
# import numpy as np
from PIL import Image, ImageOps, ImageFilter
class BaseImageManager(ABC):
    @abstractmethod
    def preprocess_image(self, pil_image: Image.Image) -> Image.Image:
        pass

    @abstractmethod
    def extract_text_from_image(self, image: Image.Image) -> str:
        pass