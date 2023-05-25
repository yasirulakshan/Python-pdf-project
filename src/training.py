from langchain.document_loaders import PagedPDFSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import os


def split_pdf_pages(path):
    """
    Splits a PDF document into individual pages.

    Parameters:
        path (str): The path to the PDF document to be split.

    Returns:
        pages (list): A list of individual pages obtained from the PDF document.
    """
    loader = PagedPDFSplitter(path)
    pages = loader.load_and_split()
    return pages


def create_faiss_index(pages):
    """
    Creates a FAISS (Facebook AI Similarity Search) index for a collection of pages.

    Parameters:
        pages (list): A list of pages/documents to be indexed.

    Returns:
        faiss_index: A FAISS index created for the given pages, enabling efficient similarity search.
    """
    faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())
    return faiss_index


def save_faiss_index(faiss_index, path):
    """
    Saves a FAISS index to a local file.

    Parameters:
        faiss_index: The FAISS index to be saved.
        path (str): The path to the file where the index will be saved.

    Returns:
        None
    """
    faiss_index.save_local(path)


def train_and_save_index(file):
    """
    Trains a FAISS index by performing page splitting, indexing, and saving the index.

    Parameters:
        file (str): The path to the file containing the pages to be indexed.

    Returns:
        str: A message indicating the completion of the indexing process.
    """
    pages = split_pdf_pages(file)
    faiss_index = create_faiss_index(pages)
    save_faiss_index(faiss_index, "index")
    os.remove(file)
    return {
        "message": "Training and indexing completed successfully",
        "status": 200,
    }
