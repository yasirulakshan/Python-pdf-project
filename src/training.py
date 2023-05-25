from langchain.document_loaders import PagedPDFSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import os


# Page splitting function need to provide the path of the file
def pageSplit(path):
    loader = PagedPDFSplitter(path)
    pages = loader.load_and_split()
    return pages


# Indexing function need to provide the pages
def indexing(pages):
    faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())
    return faiss_index


# Save index function need to provide the index and path
def saveIndex(faiss_index, path):
    faiss_index.save_local(path)


# Train function need to provide the path of the file
def train(file):
    pages = pageSplit(file)
    faiss_index = indexing(pages)
    saveIndex(faiss_index, "index")
    os.remove(file)
    return "Indexing Done"
