
# Document-Based Question Answering System
This project implements a **Document-Based Question Answering System** that uses **similarity search**, **vector databases**, and **embedding models** to retrieve relevant documents based on a given query. The retrieved documents are then passed to a **Large Language Model (LLM)**, which generates the final answer. The system is designed to efficiently handle document retrieval and question answering by leveraging **LangChain** for pipeline management and **vector databases** for fast similarity search.

# Features
- **Similarity Search**: Efficiently retrieves documents that are semantically similar to the input question.
- **Embedding Model**: Creates vector representations of the data (documents) for fast similarity comparison.
- **Vector Database**: Stores the document vectors to allow scalable and efficient retrieval during the similarity search.
- **LLM Integration**: Uses a Large Language Model to generate answers based on the retrieved documents.

# Table of Contents
- Prerequisites
- Installation
- Environment Setup
- Docker Setup
- Usage with Streamlit

# Prerequisites
Ensure you have the following installed before proceeding:

- Python 3.7+
- pip (Python package manager)
- Docker 

Additionally, you will need API keys for:

- OpenAI for LLM integration.

# Installation
1. **Clone the repository:**

```bash
Copy code
git clone https://github.com/1234aje/Document-Based-QA-System.git
cd Document-Based-QA-System
```

2. **Install dependencies:**

```bash
Copy code
pip install -r requirement.txt
```

3. **Verify installations:** Ensure the following dependencies are installed:

- LangChain
- OpenAI
- Python-dotenv
- FAISS (faiss-gpu for fast similarity search)
- PyPDF (for PDF processing)
- Streamlit (for the interactive UI)

These can be found in the ``` requirement.txt```:

# Docker Setup
For containerized deployment, the project includes a ``` Dockerfile``` and ``` docker-compose.yml``` to easily manage the application's environment.

## Building and Running the Docker Container
1. **Build the Docker image:**
```bash
Copy code
docker-compose build
```

2. **Run the Docker container:**
```bash
Copy code
docker-compose up
```
This will start the application inside a container. You can interact with it via the Streamlit interface.

# Usage with Streamlit
1. **Run the Streamlit app:** The core interface of this project is built with Streamlit, allowing users to interact with the question-answering system through a browser interface.
```bash
Copy code
streamlit run main.py
```
2. **Access the app:** Once the command is run, it will open a web browser with the Streamlit UI, where you can enter a query.

# Workflow
- **Input Question:** The user provides a question via the Streamlit interface.

- **Similarity Search:** The system uses an **embedding model** to create vector representations of the documents and then performs a **similarity search** using a **vector database** (such as FAISS) to find the most relevant documents.

- **LLM Processing:**  The relevant documents are passed to the LLM, which generates the final answer.
