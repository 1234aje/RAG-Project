import os
import streamlit as st
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

def setup_retrieval_qa_system(doc_directory, question, chunk_size=200, chunk_overlap=50):
    load_dotenv()

    open_ai_key = os.getenv("OPENAI")
    if not open_ai_key:
        raise ValueError("OpenAI API key is missing. Please set it in the .env file.")
    os.environ["OPENAI_API_KEY"] = open_ai_key

    with st.spinner('Loading and processing documents...'):
        loader = DirectoryLoader(
            doc_directory,
            loader_cls=PyPDFLoader,
            glob="**/*.pdf"
        )
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        splitted_chunks = text_splitter.split_documents(docs)

        embedding_model = OpenAIEmbeddings()
        vector_db = FAISS.from_documents(splitted_chunks, embedding_model)
        retriever = vector_db.as_retriever()

    llm = ChatOpenAI()

    retrieval_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    
    with st.spinner('Finding the best answer...'):
        result = retrieval_chain.invoke(question)
    
    return result['result']

def main():
    st.title("📝 Document-Based Question Answering System")

    st.sidebar.header("Configuration")

    # File uploader for PDFs
    uploaded_files = st.sidebar.file_uploader("Upload PDF documents", type="pdf", accept_multiple_files=True)
    
    # Get the document directory from the user
    doc_directory = st.text_input("Or enter the document directory path directly:", "")

    # Set chunk size and overlap
    chunk_size = st.sidebar.slider("Set chunk size", 100, 500, 200)
    chunk_overlap = st.sidebar.slider("Set chunk overlap", 0, 100, 50)

    # Input for the question
    question = st.text_input("Enter your question:")

    # Button to trigger the QA system
    if st.button("Get Answer"):
        if uploaded_files:
            doc_directory = "/tmp/streamlit_uploaded_docs"
            os.makedirs(doc_directory, exist_ok=True)
            for file in uploaded_files:
                with open(os.path.join(doc_directory, file.name), "wb") as f:
                    f.write(file.getbuffer())
        elif not doc_directory:
            st.warning("Please upload PDF files or provide a document directory.")
            return

        if question:
            try:
                result = setup_retrieval_qa_system(doc_directory, question, chunk_size, chunk_overlap)
                st.success("Answer found!")
                st.write(f"**Answer:** {result}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please provide a question.")

if __name__ == "__main__":
    main()


