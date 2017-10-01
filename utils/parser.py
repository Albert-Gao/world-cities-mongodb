import csv
from utils.mongodb import save_cities, save_countries
from utils.paths import get_city_data_path, get_country_data_path
from models.City import City
from models.Country import Country

def read_csv_by_line(file_path, callback):
    with open(file_path) as file_to_parse:
        for line in csv.reader(file_to_parse, dialect='excel-tab'):
            if line and not line[0].startswith("#"):
                callback(line)


#########################
#   Parse the cities    #
#########################
cities = []

def parse_city_callback(line):
    city = City(line)
    cities.append(city.to_dict())

def parse_city():
    read_csv_by_line(
        get_city_data_path(), 
        parse_city_callback
    )
    save_cities(cities)


#########################
#  Parse the countries  #
#########################
countires = []

def parse_country_callback(line):
    country = Country(line)
    countires.append(country.to_dict())


def parse_country():
    read_csv_by_line(
        get_country_data_path(), 
        parse_country_callback
    )
    save_countries(countires)