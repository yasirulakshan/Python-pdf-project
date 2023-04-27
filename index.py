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
        'status': 'Server is up and running.'
    }

@app.route("/upload", methods=["POST"])
def upload():
    tc.indexPages(request.files['file'])
    return {
        'status': 'Indexing Completed.'
    }


@app.route("/ask", methods=["POST"])
def askQuestion():
    question = request.json["question"]
    answer = sc.getAnswer(question)
    return answer


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)
