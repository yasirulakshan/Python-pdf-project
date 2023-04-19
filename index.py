# Training Process
# Input : PDF file
# Spliting Strategy : Developer has a choice to split the pages as developer requirement
# Indexing Process : Indexing the pages using FAISS
# Save Index : Save the index in local storage

from flask import Flask, request
from flask_cors import CORS
from src.training import train
from src.consumer import askQuestion


app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/train", methods=["POST"])
def pdfScan():
    file = request.files["file"]
    file.save(file.filename)
    out = train(file.filename)
    return out


@app.route("/askQuestion", methods=["POST"])
def ask():
    question = request.json["question"]
    out = askQuestion(question)
    return out


@app.route("/")
def sayHello():
    return "Hello World"
