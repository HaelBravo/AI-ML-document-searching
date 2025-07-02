
from abc import ABC, abstractmethod
from PIL import Image
from llama_index.core.readers import StringIterableReader


class BaseChunker(ABC):

    @abstractmethod
    def splitting_text(self, document_content: list[str]) -> list[str]:
        pass