import csv
from utils.paths import get_city_data_path, get_country_data_path
from models.City import City

def read_csv_by_line(file_path, callback):
    with open(file_path) as file_to_parse:
        for line in csv.reader(file_to_parse, dialect='excel-tab'):
            if line and not line[0].startswith("#"):
                callback(line)

#########################
#   Parse the cities    #
#########################

def parse_city_callback(line):
    city = City(line)
    city_data = city.__dict__
    print(line)

def parse_city():
    read_csv_by_line(get_city_data_path(), parse_city_callback)



#########################
#  Parse the countries  #
#########################

def parse_country_callback(line):
    print(line)


def parse_country():
    read_csv_by_line(get_country_data_path(), parse_country_callback)