# Langchain Objectbox Demo
This project demonstrates how to use Langchain with ObjectBox to perform document retrieval and question answering. It utilizes Streamlit for the user interface and supports querying embedded documents using OpenAI and Groq models.

## Table of contents
- [Features](#features)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
---

### Features

- **Document Embedding:** Upload PDF files and convert them into vectors for efficient searching.
- **Question Answering:** Ask questions based on the embedded documents.
- **Retrieval-Augmented Generation (RAG):** Combines document retrieval with language model responses.
---

### Installation

Follow these steps to set up the project:

1. **Clone the Repository:**
```
git clone git@github.com:Pabl0Azeved0/langchain-objectbox.git
cd langchain-objectbox
```

2. **Set Up a Virtual Environment:**
```
python3 -m venv venv
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
---

### Setup

1. **Prepare your documents:**
- Place your PDF files in the `files/` directory. These documents will be used for embedding and querying, I left there 3 pdfs as examples, I strongly encourage you to delete them and use your own.

2. **Run the application:**
- Start the streamlit application using the Makefile by running the command `make run` on your terminal. This will open a web interface where you can interact with the application, if one is not opened try reading the terminal or simply typing in your favorite browser the link `http://localhost:8501/`
---

### Usage

1. **Run the application:**
- First make sure you are inside your venv where every package should be installed and run your project, here's a snippet to make it easier:
```
make run
```
- Then you should be seeing something like this: ![](https://i.imgur.com/z1Z4zpo.png)
2. **Embedding Documents:**
- Click on the "Documents Embedding" button to load and embed the PDF documents. The application will process the documents and prepare them for querying, after the process is over you should be seeing something like this: ![](https://i.imgur.com/6nox9Qu.png)
3. **Ask Questions:**
- Enter your question in the text input field. The application will use the embedded documents to provide an answer, after the process it will return the original question to you along with the answer, this should be the result: ![](https://i.imgur.com/NoBJSde.png)
4. **View Document Similarity:**
- Expand the "Document Similarity Search" section to see the context of documents related to your query. ![](https://i.imgur.com/4Sc7bah.png)
5. **The project:**
- After that you should see your project file like this:
    - ![](https://i.imgur.com/oDMUAO5.png)
- But don't worry, it's just temporary files, the `objectbox` folder is actually the "database", that's why I created 3 makefile commands to clean this up:
    - `make clean`: Cleans up both pycache and objectbox folders
    - `make clean-cache`: Only cleans up the pycache
    - `make clean-database`: Only cleans up the objectbox
- After cleaning up your project should be fine, but keep in mind once you clean the objectbox you'll have to embed every document again by clicking on the button.
