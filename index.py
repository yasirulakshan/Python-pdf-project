from flask import Flask, request
from flask_cors import CORS
import functions

app = Flask(__name__)

CORS(app, supports_credentials=True)


@app.route("/train")
def pdfScan():
    pages = functions.pageSplit("./99x-awardsv2.pdf")
    functions.indexing(pages)
    return {
        'status': 'Indexing Completed.'
    }


@app.route("/ask-question", methods=["POST"])
def askQuestion():
    question = request.json["question"]
    result = functions.searchText(question)
    answer = functions.getExactAnswer(result, question)
    return answer
