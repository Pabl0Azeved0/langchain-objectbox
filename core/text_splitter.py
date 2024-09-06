from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_text_splitter():
    """Return an instance of RecursiveCharacterTextSplitter."""
    return RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
