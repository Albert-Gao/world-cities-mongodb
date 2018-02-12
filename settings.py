MONGO_HOST = 'localhost'
MONGO_PORT = 27017
DB_NAME = 'WorldCities'

CITY_COLLECTION_NAME = 'cities'
COUNTRY_COLLECTION_NAME = 'countries'

# Only countries with languages below.
# Find the languages here:
# http://www.lingoes.net/en/translator/langcode.htm
# city.country_code and country.iso MUST be there in order to enable this feature.
# Below is an example for only save all English speaking countries.
ONLY_LANGUAGE = [
    # 'en',
    # 'en-AU', 'en-BZ', 'en-CA', 'en-CB',
    # 'en-GB', 'en-IE', 'en-JM', 'en-NZ',
    # 'en-PH', 'en-TT', 'en-US', 'en-ZA',
    # 'en-ZW'
]

# Add the name of field that you don't want to save to the database
# For instance, You don't want to save the alternate_names to cities collection
# Just add it: CITY_FIELDS_BLACKLIST = [ 'alternate_names' ]
# The BLACKLIST is always a list.
CITY_FIELDS_BLACKLIST = [
    'feature_class',
    'feature_code',
    'admin1_code',
    'admin2_code',
    'admin3_code',
    'admin4_code',
    'population',
    'elevation',
    'dem',
    'latitude',
    'longitude',
    'cc2',
    'modification_date'
]
COUNTRY_FIELDS_BLACKLIST = [
    'iso3',
    'iso_numeric',
    'fips',
    'area',
    'population',
    'continent',
    'tld',
    'equivalent_fips_code',
    'neighbours'
]

# It will duplicate a little data to prevent joint queries
# So after you retrieve the city info, you don't need to query the according
# country info using `geo_name_id`, there will be a country property for you. Vice versa
# And you can customize the fields as well
# The `geo_name_id` will always be added in case you need to refer each other
ADD_CITY_TO_COUNTRY = True
CITY_FIELDS_TO_ADD = ['name']

ADD_COUNTRY_TO_CITY = True
COUNTRY_FIELDS_TO_ADD = [
    'iso',
    'country', 
    'currency_code', 
    'currency_symbol'
]
