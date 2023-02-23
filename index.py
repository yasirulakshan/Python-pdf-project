from langchain.document_loaders import PagedPDFSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import os
import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = "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"


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
        results += doc.page_content
    return results


def getExactAnswer(result, question):
    prompt = """Answer the question as truthfully as possible using the provided text, and if the answer is not contained within the text below, say "I don't know\n""" + result + "\n\n" + question + "\n"
    answer = openai.Completion.create(
        prompt=prompt,
        temperature=0.7,
        max_tokens=300,
        model="text-ada-001"
    )["choices"][0]["text"].strip(" \n")
    return answer


# pages = pageSplit("Confluence.pdf")
# faiss_index = indexing(pages)
# saveIndex(faiss_index, "index")
faiss_index = loadIndex("index")
result = searchText(faiss_index, "What is the purpose of the audit?")
answer = getExactAnswer(result, "What is the purpose of the audit?")
print(answer)
