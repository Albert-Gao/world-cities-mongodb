from pymongo import MongoClient
from utils.parser import cities, countries, cities_dict, countries_dict
from urllib.parse import quote_plus
import settings

if settings.MONGO_USER and settings.MONGO_PASSWORD:
    URI = "mongodb://%s:%s@%s:%s/%s" % (quote_plus(settings.MONGO_USER), quote_plus(settings.MONGO_PASSWORD), settings.MONGO_HOST, settings.MONGO_PORT, settings.DB_NAME)
else:
    URI = "mongodb://%s:%s/%s" % (settings.MONGO_HOST, settings.MONGO_PORT, settings.DB_NAME)

MONGO_CLIENT = MongoClient(URI)
DB = MONGO_CLIENT[settings.DB_NAME]
CITY_COLLECTION = DB[settings.CITY_COLLECTION_NAME]
COUNTRY_COLLECTION = DB[settings.COUNTRY_COLLECTION_NAME]

def init():
    CITY_COLLECTION.drop()
    COUNTRY_COLLECTION.drop()

#################
#  Save cities  #
#################

def add_extra_country_fields():
    if not settings.ADD_COUNTRY_TO_CITY:
        return

    for city in cities:
        according_country = countries_dict[city['country_code']]
        attrs_to_add = {
            'country_id': according_country.country_id
        }
        for attr in settings.COUNTRY_FIELDS_TO_ADD:
            attrs_to_add[attr] = getattr(according_country, attr)

        city['country'] = attrs_to_add

def save_cities():
    add_extra_country_fields()
    save_to_db(CITY_COLLECTION, cities)

def add_extra_cities_fields():
    if not settings.ADD_CITY_TO_COUNTRY:
        return
    
    for country in countries:
        if country['iso'] in cities_dict:
            country['cities'] = cities_dict[country['iso']]

####################
#  Save countries  #
####################

def save_countries():
    add_extra_cities_fields()
    save_to_db(COUNTRY_COLLECTION, countries)

def save_to_db(mongo_collection, data):
    if not isinstance(data, list):
        raise ValueError('Except data to be a list')

    if not isinstance(data[0], dict):
        raise ValueError('Except item of data to be a dict')

    mongo_collection.insert_many(data)
