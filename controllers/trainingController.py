from langchain.document_loaders import PagedPDFSplitter
from langchain.vectorstores import Milvus
from langchain.embeddings.openai import OpenAIEmbeddings
import openai

import random
import string
from werkzeug.utils import secure_filename

import milvus as mvs

from controllers.dataController import dataController

class trainingController:

    dc = None
    
    def __init__(self):
        self.dc = dataController()
        openai.api_key = self.dc.getOpenAIAPIKey()


    def pageSplit(self,path):
        loader = PagedPDFSplitter(path)
        pages = loader.load_and_split()
        return pages
    
    def saveFile(self,file):
        file_name = secure_filename(file.filename)
        random_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        new_filename = random_name + '.' + file_name.split('.')[1]
        file.save("./data/" + new_filename)
        return new_filename


    def indexPages(self,file):

        new_filename = self.saveFile(file)
        pages = self.pageSplit("./data/" + new_filename)

        milvus_db = Milvus.from_documents(
            documents=pages,
            embedding=OpenAIEmbeddings(openai_api_key=self.dc.getOpenAIAPIKey()),
            #connection_args={"host": "127.0.0.1", "port": "19530"},
        )

        

        return milvus_db