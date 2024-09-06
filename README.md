# Langchain Objectbox Demo
This project demonstrates how to use Langchain with ObjectBox to perform document retrieval and question answering. It utilizes Streamlit for the user interface and supports querying embedded documents using OpenAI and Groq models.

## Table of contents
- [Features](#features)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)


### Features

- **Document Embedding:** Upload PDF files and convert them into vectors for efficient searching.
- **Question Answering:** Ask questions based on the embedded documents.
- **Retrieval-Augmented Generation (RAG):** Combines document retrieval with language model responses.

### Installation

Follow these steps to set up the project:

1. **Clone the Repository:**
```
git clone here
cd sofya-langchain
```

2. **Set Up a Virtual Environment:**
```
python -m venv venv
source venv/bin/activate
```

3. **Install Dependencies:**
- A Makefile was created to make it easier so use it :grin:
> [!WARNING]
> Please make sure you are inside your venv (`source venv/bin/activate`), your terminal should have (venv) at the beginning.

```
make install
```

4. **Set Up Environment Variables:**
- Create a `.env` file in the root directory with the following content:
```
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```
- Replace `your_openai_api_key` and `your_groq_api_key` with your actual API keys.
If you have any trouble on getting your OPENAI api key, [this can help you](https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key) and if you have trouble getting your GROQ api key, [get help here](https://console.groq.com/docs/quickstart).


### Setup

1. **Prepare your documents:**
- Place your PDF files in the `files/` directory. These documents will be used for embedding and querying, I left there 3 pdfs as examples, I strongly encourage you to delete them and use your own.

2. **Run the application:**
- Start the streamlit application using the Makefile by running the command `make run` on your terminal. This will open a web interface where you can interact with the application, if one is not opened try reading the terminal or simply typing in your favorite browser the link `http://localhost:8501/`


### Usage

1. **Embedding Documents:**
- Click on the "Documents Embedding" button to load and embed the PDF documents. The application will process the documents and prepare them for querying.
2. **Ask Questions:**
- Enter your question in the text input field. The application will use the embedded documents to provide an answer.
3. **View Document Similarity:**
- Expand the "Document Similarity Search" section to see the context of documents related to your query.
