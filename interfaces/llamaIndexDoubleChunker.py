from llama_index.core.node_parser import (
    SemanticDoubleMergingSplitterNodeParser,
    LanguageConfig,
)
#from llama_index.core import SimpleDirectoryReader
from llama_index.core.readers import StringIterableReader


from my_app.interfaces.baseChunker import BaseChunker

class LlamaIndexDoubleChunker(BaseChunker):

    def __init__(self):
        self.string_iterable_reader = StringIterableReader()

    def splitting_text(self, document_content: list[str]) -> list[str]:
        documents = self.string_iterable_reader.load_data(document_content)
        config = LanguageConfig(language="english", spacy_model="en_core_web_md")
        splitter = SemanticDoubleMergingSplitterNodeParser(
            language_config=config,
            initial_threshold=0.4,
            appending_threshold=0.5,
            merging_threshold=0.5,
            max_chunk_size=5000,
        )
        nodes = splitter.get_nodes_from_documents(documents)

        return [e.get_content() for e in nodes]