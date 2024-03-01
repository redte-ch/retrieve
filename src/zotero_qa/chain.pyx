"""The chain for the QA."""

from langchain.chains import RetrievalQA

from llm import LLM
from prompt import Prompt
from store import Store

# The prompt template object.
prompt = Prompt()

# The vector store object.
store = Store()

# The Ollama LLM object.
llm = LLM()


class Chain(RetrievalQA):
    """The RetrievalQA chain class."""

    @classmethod
    def from_chain(cls) -> RetrievalQA:
        """Create a new chain from the current chain type."""
        return cls.from_chain_type(
            chain_type_kwargs={"prompt": prompt},
            llm=llm,
            retriever=store.as_retriever(),
            return_source_documents=True,
        )
