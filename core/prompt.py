from langchain_core.prompts import ChatPromptTemplate

def create_prompt():
    """Create and return a ChatPromptTemplate."""
    return ChatPromptTemplate.from_template(
        """
        Answer the questions based on the provided context only.
        Please provide the most accurate response based on the question
        <context>
        {context}
        <context>
        Questions:{input}
        """
    )
