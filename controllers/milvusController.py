from pymilvus import (
    connections,
    utility,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
)

class milvusController:

    def __init__(self) -> None:
        connections.connect("default", host="localhost", port="19530")

    def getCollections(self):
        return utility.list_collections()
    
    def getCollectionInfo(self,collectionName):
        return Collection(collectionName).schema.to_dict()


    
