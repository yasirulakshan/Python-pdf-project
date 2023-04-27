from flask import Flask, request
from flask_cors import CORS
from controllers.trainingController import trainingController
from controllers.searchController import searchController

app = Flask(__name__)

CORS(app, supports_credentials=True)


tc = trainingController()
sc = searchController()

@app.route("/")
def status():
    return {
        'status': 'Server is running.'
    }

@app.route("/train")
def pdfScan():
    pages = tc.pageSplit("./data/99x-awardsv2.pdf")
    tc.indexPages(pages)
    return {
        'status': 'Indexing Completed.'
    }


@app.route("/ask-question", methods=["POST"])
def askQuestion():
    question = request.json["question"]
    result = sc.searchText(question)
    answer = sc.getExactAnswer(result, question)
    return answer


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)
