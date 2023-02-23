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

def loadIndex(path):
    faiss_index = FAISS.load_local(path, OpenAIEmbeddings())
    return faiss_index

def searchText(faiss_index, question):
    docs = faiss_index.similarity_search(question, k=2)
    results = ""
    for doc in docs:
        results+=doc.page_content
    return results