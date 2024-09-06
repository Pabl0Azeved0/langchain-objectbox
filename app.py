import streamlit as st
import time
import os
from config.config import load_configuration
from core.embeddings import get_openai_embeddings
from core.pdf_loader import load_pdfs
from core.vector_store import create_objectbox_store
from core.text_splitter import get_text_splitter
from core.prompt import create_prompt
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

# Load environment variables
load_configuration()

# Set up Streamlit title
st.title("Langchain Objectbox Demo")

# Initialize core components
llm = ChatGroq(
    groq_api_key=os.getenv('GROQ_API_KEY'),
    model_name="Llama3-8b-8192"
)
prompt = create_prompt()

def vector_embedding():
    """Load and process PDF documents, then create vector embeddings."""
    if "vectors" not in st.session_state:
        st.session_state.embeddings = get_openai_embeddings()
        st.session_state.loader = load_pdfs("./files")
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = get_text_splitter()
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(
            st.session_state.docs[:20]
        )
        st.session_state.vectors = create_objectbox_store(
            st.session_state.final_documents,
            st.session_state.embeddings
        )

input_prompt = st.text_input(
    "Enter your question based on the documents embedded:"
)

if st.button("Documents Embedding"):
    vector_embedding()
    st.write("ObjectBox Database is ready")

if input_prompt:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    start = time.process_time()

    response = retrieval_chain.invoke({'input': input_prompt})

    st.write(f"Original question: {input_prompt}.\n\n{response['answer']}")

    with st.expander("Document Similarity Search"):
        for i, doc in enumerate(response['context']):
            st.write(doc.page_content)
            st.write("------------------------------")
