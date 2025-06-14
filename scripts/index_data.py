import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

pdf_dir= "data/raw_pdfs"
all_docs =[]
for fname in os.listdir(pdf_dir):
    if fname.endswith(".pdf"):
        loader= PyPDFLoader(os.path.join(pdf_dir,fname))
        all_docs.extend(loader.load())

splitter= RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
docs =splitter.split_documents(all_docs)

embedding= HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
faiss_store =FAISS.from_documents(docs, embedding)
faiss_store.save_local("data/db")

