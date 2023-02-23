from langchain.document_loaders import PagedPDFSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

def pageSplit(path):
    loader = PagedPDFSplitter(path)
    pages = loader.load_and_split()
    return pages

def indexing(pages):
    faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())   
    return faiss_index

def saveIndex(faiss_index, path):
    faiss_index.save_local(path)


