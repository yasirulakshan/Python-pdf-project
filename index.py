

# Training Process
# Input : PDF file
# Spliting Strategy : Developer has a choice to split the pages as developer requirement
# Indexing Process : Indexing the pages using FAISS
# Save Index : Save the index in local storage

from flask import Flask, request
from flask_cors import CORS
from src.training import train_and_save_index
from src.consumer import ask_question


app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/train", methods=["POST"])
def train_and_index_pdf():
    """
    Endpoint for training and indexing a PDF file.

    Expects a PDF file in the request's "file" field.
    Saves the file locally, performs training and indexing,
    and returns the output message indicating the completion of the process.
    """
    file = request.files["file"]
    file.save(file.filename)
    out = train_and_save_index(file.filename)
    return out


@app.route("/askQuestion", methods=["POST"])
def ask_question_endpoint():
    """
    Endpoint for asking a question and generating an answer.

    Expects a JSON object in the request body with a "question" field.
    Calls the ask_question function to generate an exact answer to the question,
    and returns the generated answer as the response.
    """
    question = request.json["question"]
    out = ask_question(question)
    return out


@app.route("/")
def hello_endpoint():
    """
    Endpoint for checking the backend's status.

    Returns a simple message indicating that the backend is running properly.
    """
    return {
        "message": "Backend is running properly",
        "status": 200,
    }
