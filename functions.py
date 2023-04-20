from langchain.document_loaders import PagedPDFSplitter
from langchain.vectorstores import Milvus
from langchain.embeddings.openai import OpenAIEmbeddings
import openai

A = "sk-0pxxQ"
P = "nATUPRy"
I = "pWTlx6Ot"
K = "T3BlbkFJI"
E = "us4t9zQ3SG"
Y = "4dU2MjeSU"

open_ai_api_key = A+P+I+K+E+Y


def searchText(question):
    milvus = Milvus(
        collection_name='c3acd1f1f66b34d739cb0c9ca31b12d65',
        connection_args={"host": "127.0.0.1", "port": "19530"},
        embedding_function=OpenAIEmbeddings(openai_api_key=open_ai_api_key),
        text_field='c4165f70d58b049d0b866af3e4671a6e1'
    )
    docs = milvus.similarity_search(question, k=2)
    results = ''
    for doc in docs:
        results += doc.page_content
    return results


def pageSplit(path):
    loader = PagedPDFSplitter(path)
    pages = loader.load_and_split()
    return pages


def indexing(pages):
    milvus_db = Milvus.from_documents(
        documents=pages,
        embedding=OpenAIEmbeddings(openai_api_key=open_ai_api_key),
        connection_args={"host": "127.0.0.1", "port": "19530"},
    )
    return milvus_db


def searchText(question):
    milvus = Milvus(
        collection_name='c3acd1f1f66b34d739cb0c9ca31b12d65',
        connection_args={"host": "127.0.0.1", "port": "19530"},
        embedding_function=OpenAIEmbeddings(openai_api_key=open_ai_api_key),
        text_field='c4165f70d58b049d0b866af3e4671a6e1'
    )
    docs = milvus.similarity_search(question, k=2)
    results = ''
    for doc in docs:
        results += doc.page_content
    return results


def getExactAnswer(result, question):
    prompt = """You are an AI assistant in a conversation with a human. \n Answer their questions as truthfully as possible using the provided text. If the answer is not contained within the text, say "I dont have that knowlege.". """ + \
        result + "\n\n Q:" + question + "\n"
    result = openai.Completion.create(
        prompt=prompt,
        temperature=0.7,
        max_tokens=300,
        model="text-davinci-003",
        top_p=1,
    )["choices"][0]["text"].lstrip("A: ")
    return {
        'answer': result.replace('\n', '').strip()
    }
