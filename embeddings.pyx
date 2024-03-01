"""Helper class to wrap the Ollama embeddings."""

import alive_progress
from langchain_community.embeddings import OllamaEmbeddings


class Embeddings:
    """Wrapper for the Ollama embeddings."""

    def __init__(self, model_name: str) -> None:
        """Create a new Ollama embeddings object."""
        self.embedding = OllamaEmbeddings(model=model_name)

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """Embed a list of documents."""
        print("    Generating embeddings...")
        embeddings = []
        with alive_progress.alive_bar(len(texts)) as bar:
            for text in texts:
                embeddings += self.embedding.embed_documents([text])
                bar()
        return embeddings

    def embed_query(self, query: str) -> list[float]:
        """Embed a query."""
        return self.embedding.embed_query(query)
