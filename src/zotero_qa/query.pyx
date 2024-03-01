"""Query from local embeddings from Zotero PDFs using Ollama and Chroma."""

import warnings

from chain import Chain

# Suppress warnings.
warnings.filterwarnings("ignore")

# The QA chain object.
chain = Chain.from_chain()


def query(question: str) -> None:
    """Query the local embeddings for the answer to the question."""
    answer = chain(question)
    source = answer.get("source_documents")
    if source:
        print("\n\nSources:")
        for file in source:
            print(f"  - {file.metadata['source'].split('/')[-1]}")
