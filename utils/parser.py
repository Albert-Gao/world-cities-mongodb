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
countries = []
countries_dict = {}
match_language_countries_iso = []

def parse_country_callback(line):
    country = Country(line)
    countries.append(country.to_dict())
    if settings.ADD_COUNTRY_TO_CITY:
        countries_dict[country.iso] = country

    if settings.ONLY_LANGUAGE:
        for language in country.languages:
            if language in settings.ONLY_LANGUAGE:
                match_language_countries_iso.append(country.iso)
                break

def parse_country():
    read_csv_by_line(
        get_country_data_path(),
        parse_country_callback
    )

# Extra filter:
# To only add the countries and cities which use language in settings.ONLY_LANGUAGE
# We can filter the contries when processing to gain more performance
# But I like to keep they all here to cleaner logic.
def remove_non_match_language_countries_and_cities():
    if not settings.ONLY_LANGUAGE: 
        return

    print(match_language_countries_iso)

    cities[:] = [c for c in cities if c['country_code'] in match_language_countries_iso]
    countries[:] = [c for c in countries if c['iso'] in match_language_countries_iso]
