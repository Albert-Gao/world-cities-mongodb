MONGO_HOST = 'localhost'
MONGO_PORT = 27017
DB_NAME = 'WorldCities'

CITY_COLLECTION_NAME = 'City'
COUNTRY_COLLECTION_NAME = 'Country'

# Add the name of field that you don't want to save to the database
# For instance, You don't want to save the alternate_names from cities collection
# Just add it: CITY_FIELDS_BLACKLIST = [ 'alternate_names' ]
# The BLACKLIST is always a list.
CITY_FIELDS_BLACKLIST = []
COUNTRY_FIELDS_BLACKLIST = []
