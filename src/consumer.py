import openai
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings


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
    prompt = """You are an AI assistant in a conversation with a human. \n Answer their questions as truthfully as possible using the provided text. If the answer is not contained within the text, say "I haven't that knowlege.". """ + \
        result + "\n\n Q:" + question + "\n"
    answer = openai.Completion.create(
        prompt=prompt,
        temperature=0.7,
        max_tokens=300,
        model="text-davinci-003",
        top_p=1,
    )["choices"][0]["text"].strip(" \n")
    return answer


def askQuestion(question):
    faiss_index = loadIndex("index")
    result = searchText(faiss_index, question)
    answer = getExactAnswer(result, question)
    answer = answer.lstrip("A: ")
    return answer
