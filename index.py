# Training Process
# Input : PDF file
# Spliting Strategy : Developer has a choice to split the pages as developer requirement
# Indexing Process : Indexing the pages using FAISS
# Save Index : Save the index in local storage

import openai
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


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


@app.route("/train")
def pdfScan():
    pages = pageSplit("./99x-awardsv2.pdf")
    faiss_index = indexing(pages)
    saveIndex(faiss_index, "index")
    return "Indexing Done"


@app.route("/askQuestion", methods=["POST"])
def askQuestion():
    question = request.json["question"]
    faiss_index = loadIndex("index")
    result = searchText(faiss_index, question)
    answer = getExactAnswer(result, question)
    answer = answer.lstrip("A: ")
    return answer


@app.route("/")
def sayHello():
    return "Hello World"
