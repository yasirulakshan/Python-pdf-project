from langchain.vectorstores import Milvus
from langchain.embeddings.openai import OpenAIEmbeddings
import openai
from controllers.dataController import dataController

class searchController:

    dc = None
    
    def __init__(self):
        self.dc = dataController()
        openai.api_key = self.dc.getOpenAIAPIKey()

    def search(self,text):
        milvus = Milvus(
            collection_name='c3acd1f1f66b34d739cb0c9ca31b12d65',
            connection_args={"host": "127.0.0.1", "port": "19530"},
            embedding_function=OpenAIEmbeddings(openai_api_key=self.dC.getOpenAIAPIKey()),
            text_field='c4165f70d58b049d0b866af3e4671a6e1'
        )
        docs = milvus.similarity_search(text, k=2)
        results = ''
        for doc in docs:
            results += doc.page_content
        return results


    def getAnswer(self,result, question):

        information = self.search(question)
        

        result = openai.Completion.create(
            prompt= dC.getConstructedChat(information, question),
            temperature=0.7,
            max_tokens=600,
            model="text-davinci-003",
            top_p=1,
        )


        return {
            'answer': result["choices"][0]["text"]
        }