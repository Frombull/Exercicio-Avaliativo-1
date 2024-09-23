from dataset import dataset
import pymongo


class Database:
    def __init__(self, database, collection):
        self.clusterConnection = None
        self.collection = None
        self.db = None

        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connection_string = "mongodb+srv://marco:hunter2@clusterbosta.atsfp.mongodb.net/"
            self.clusterConnection = pymongo.MongoClient(
                connection_string,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao BD")
        except Exception as e:
            print(e)

    def reset_database(self):
        try:
            self.db.drop_collection(self.collection)
            self.collection.insert_many(dataset)
            print("BD resetado")
        except Exception as e:
            print(e)
