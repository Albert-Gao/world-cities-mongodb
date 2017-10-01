from pymongo import MongoClient
import settings

MONGO_CLIENT = MongoClient(settings.MONGO_HOST, settings.MONGO_PORT)
DB = MONGO_CLIENT[settings.DB_NAME]
CITY_COLLECTION = DB[settings.CITY_COLLECTION_NAME]
COUNTRY_COLLECTION = DB[settings.COUNTRY_COLLECTION_NAME]

def init():
    CITY_COLLECTION.drop()
    COUNTRY_COLLECTION.drop()

def save_cities(data):
    save_to_db(CITY_COLLECTION, data)

def save_countries(data):
    save_to_db(COUNTRY_COLLECTION, data)

def save_to_db(mongo_collection, data):
    if not isinstance(data, list):
        raise ValueError('Except data to be a list')

    if not isinstance(data[0], dict):
        raise ValueError('Except item of data to be a dict')

    mongo_collection.insert_many(data)
