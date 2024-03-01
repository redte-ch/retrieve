"""Template for the prompt."""

from langchain.prompts import PromptTemplate

# The template for the prompt.
template = """
    Tu es mon assistant.
    Fais ce que je te dis.
    Basée sur mes documents, réponds aux questions.
    Réponds toujours en français, même si les documents ne le sont pas.
    Context: {context}
    User: {question}
    Chatbot:"" 
"""


class Prompt(PromptTemplate):
    """Prompt for the model."""

    def __init__(self) -> None:
        super().__init__(
            input_variables=["context", "question"],
            template=template,
        )
