from flask import Flask, request
from flask_cors import CORS
from controllers.trainingController import trainingController
from controllers.searchController import searchController
from controllers.milvusController import milvusController

app = Flask(__name__)

CORS(app, supports_credentials=True)


tc = trainingController()
sc = searchController()
ms = milvusController()

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


@app.route("/utilities", methods=["POST"])
def utilities():
    cols = ms.getCollections()
    schemaInfo = ms.getCollectionInfo(cols[0])

    print(schemaInfo)

    return {
        'collections': cols,
        'info': ms.getCollectionInfo(cols[0])
    }

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)
