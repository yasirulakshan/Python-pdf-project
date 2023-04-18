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


def train():
    pages = pageSplit("./99x-awardsv2.pdf")
    faiss_index = indexing(pages)
    saveIndex(faiss_index, "index")
    return "Indexing Done"
