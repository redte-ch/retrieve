"""Create local embeddings of Zotero PDFs using Ollama and Chroma."""

import sys

from embed import embed
from query import query

if __name__ == "__main__":
    if sys.argv[1] == "embed":
        # The maximum number of chunks to process.
        max_chunks = int(sys.argv[2]) if len(sys.argv) > 2 else 50

        # Embed the PDFs.
        embed(max_chunks)

        print("Done!")

    elif sys.argv[1] == "query":
        # The query.
        question = str(sys.argv[2])

        # Query the embeddings.
        query(question)
