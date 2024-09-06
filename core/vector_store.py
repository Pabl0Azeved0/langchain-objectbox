from langchain_objectbox.vectorstores import ObjectBox

def create_objectbox_store(documents, embeddings):
    """Create and return an ObjectBox vector store."""
    return ObjectBox.from_documents(
        documents,
        embeddings,
        embedding_dimensions=768
    )
