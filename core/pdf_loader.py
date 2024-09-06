from langchain_community.document_loaders import PyPDFDirectoryLoader

def load_pdfs(directory: str):
    """Return an instance of PyPDFDirectoryLoader."""
    return PyPDFDirectoryLoader(directory)
