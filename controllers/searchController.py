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
            collection_name='cb79ac1c1fc664b97a26e80e39b802182',
            connection_args={"host": "127.0.0.1", "port": "19530"},
            embedding_function=OpenAIEmbeddings(openai_api_key=self.dc.getOpenAIAPIKey()),
            text_field='c2067f806e2fe4aee9eefc470884e94bb'
        )
        docs = milvus.similarity_search(text, k=2)
        results = ''
        for doc in docs:
            results += doc.page_content
        return results


    def getAnswer(self, question):

        information = self.search(question)

        result = openai.Completion.create(
            prompt= self.dc.getConstructedChat(information, question),
            temperature=0.7,
            max_tokens=600,
            model="text-davinci-003",
            top_p=1,
        )


        return {
            'answer': result["choices"][0]["text"]
        }