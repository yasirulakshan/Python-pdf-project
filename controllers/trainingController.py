from langchain.document_loaders import PagedPDFSplitter
from langchain.vectorstores import Milvus
from langchain.embeddings.openai import OpenAIEmbeddings
import openai

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


    def indexPages(self,pages):
        milvus_db = Milvus.from_documents(
            documents=pages,
            embedding=OpenAIEmbeddings(openai_api_key=self.dc.getOpenAIAPIKey()),
            connection_args={"host": "127.0.0.1", "port": "19530"},
        )
        return milvus_db