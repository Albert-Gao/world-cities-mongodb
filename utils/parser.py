import csv
from utils.paths import get_city_data_path, get_country_data_path
from models.City import City
from models.Country import Country
import settings

def read_csv_by_line(file_path, callback):
    with open(file_path) as file_to_parse:
        for line in csv.reader(file_to_parse, dialect='excel-tab'):
            if line and not line[0].startswith("#"):
                callback(line)


#########################
#   Parse the cities    #
#########################
cities = []
cities_dict = {}

def save_extra_city_fields(city):
    def get_attrs_to_add():
        attrs_to_add = {
            'city_id': getattr(city, 'city_id')
        }
        for attr in settings.CITY_FIELDS_TO_ADD:
            attrs_to_add[attr] = getattr(city, attr)
        return attrs_to_add

    if not settings.ADD_CITY_TO_COUNTRY:
        return
    
    if not city.country_code in cities_dict:
        cities_dict[city.country_code] = []
    
    cities_dict[city.country_code].append(get_attrs_to_add())

def parse_city_callback(line):
    city = City(line)
    cities.append(city.to_dict())
    save_extra_city_fields(city)
    
def parse_city():
    read_csv_by_line(
        get_city_data_path(), 
        parse_city_callback
    )


#########################
#  Parse the countries  #
#########################
countires = []
countries_dict = {}

def parse_country_callback(line):
    country = Country(line)
    countires.append(country.to_dict())
    if settings.ADD_COUNTRY_TO_CITY:
        countries_dict[country.iso] = country


def parse_country():
    read_csv_by_line(
        get_country_data_path(), 
        parse_country_callback
    )
