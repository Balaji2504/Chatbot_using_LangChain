import os
from langchain.chat_models import google_palm
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import GooglePalmEmbeddings
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

# Take environment variables from .env.
load_dotenv()

# Create embeddings
vectordb_file_path = "faiss_index"

# Create Google Palm LLM model
llm = google_palm.ChatGooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"])

embeddings = GooglePalmEmbeddings()

def create_vector_db():
    # Load data
    loader = UnstructuredURLLoader(urls=["https://chettinadvidyashram.org/,https://chettinadvidyashram.org/our-school/management-board-members/"])
    data = loader.load()

    # Split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", ","],
        chunk_size=1000,
        chunk_overlap=200
    )
    docs = text_splitter.split_documents(data)

    # Save the embeddings to FAISS index
    vectordb = FAISS.from_documents(docs, embeddings)

    # Save vector database locally
    vectordb.save_local(vectordb_file_path)

def get_qa_chain():
    # Load the vector database from the local folder
    vectordb = FAISS.load_local(vectordb_file_path, embeddings)

    # Create a retriever for querying the vector database
    retriever = vectordb.as_retriever(score_threshold=0.7)

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        input_key="query"
    )
    return chain