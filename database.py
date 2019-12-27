import pymongo

__author__ = 'Cate'

class Database():
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    # uri = "mongodb://127.0.0.1:27017"
    # client = pymongo.MongoClient(uri)
    # database = client['fullstack']
    # collection = database['students']

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['mydbnamehere'] #TODO Add db name here

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find (collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
