"""Wrappper for the LLM model."""

import os

import dotenv
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms import Ollama

# Load the environment variables.
dotenv.load_dotenv()

# The name of the Ollama model to use.
model_name = os.getenv("MODEL_NAME")


class LLM(Ollama):
    """LLM model."""

    def __init__(self) -> None:
        super().__init__(
            base_url="http://localhost:11434",
            callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
            model=model_name,
        )
