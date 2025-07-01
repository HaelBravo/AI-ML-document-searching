from abc import ABC, abstractmethod
from PIL import Image

class BaseLoader(ABC):

    @abstractmethod
    def load(self, file: bytes) -> list[Image.Image]:
        pass  # No implementation in base class

