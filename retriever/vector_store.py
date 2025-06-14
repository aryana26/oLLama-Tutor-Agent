from langchain_community.vectorstores import FAISS # OG FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

def load_vector_store(persist_dir="data/db"):
    embedding= HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.load_local(folder_path=persist_dir,embeddings=embedding,allow_dangerous_deserialization=True) # scary
