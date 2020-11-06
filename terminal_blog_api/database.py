import pymongo

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize(db_name):
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client[db_name] 
    @staticmethod
    def insert(collection_name,data):
        Database.DATABASE[collection_name].insert(data)

    @staticmethod
    def find(collection_name,data):
        return Database.DATABASE[collection_name].find(data)

    @staticmethod
    def find_one(collection_name,data):
        return Database.DATABASE[collection_name].find_one(data)

