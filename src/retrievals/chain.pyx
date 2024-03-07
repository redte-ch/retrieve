#  Copyleft (ɔ) 2024 Red Innovation.
#
#  Author: Mauko Quiroga-Alvarado <mauko@redte.ch>
#
#  Licensed under the EUPL-1.2-or-later licence.
#  For details: https://joinup.ec.europa.eu/collection/eupl/eupl-text-eupl-12

#  cython: language_level=3

"""The chain for the QA."""

import os

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama

from zotero_qa import Store

# The name of the Ollama model to use.
model_name = os.getenv("MODEL_NAME")

# The template for the prompt.
template = """
    Tu es mon assistant.
    Fais ce que je te dis.
    Basé ou basée sur mes documents, réponds aux questions.
    Réponds toujours en français, même si les documents ne le sont pas.
    Context: {context}
    User: {question}
    Chatbot:""
"""

# The prompt template object.
prompt = PromptTemplate(
            input_variables=["context", "question"],
            template=template,
        )

# The vector store object.
store = Store()

# The Ollama LLM object.
llm = Ollama(
            base_url="http://localhost:11434",
            callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
            model=model_name,
        )


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
