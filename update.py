import urllib.request
import zipfile
import shutil
import os
from utils.paths import get_country_data_path, get_city_data_path

def download_file(url, file_name):
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        data = response.read() # a `bytes` object
        out_file.write(data)

def unzip_file(path_to_zip_file, directory_to_extract_to):
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    zip_ref.extractall(directory_to_extract_to)
    zip_ref.close()

def save_file():
    country_file_name = 'countryInfo.txt'
    download_file('http://download.geonames.org/export/dump/countryInfo.txt', country_file_name)
    shutil.copy(country_file_name, get_country_data_path())
    os.remove(os.path.join(os.getcwd(), country_file_name))

def save_zip():
    cities_zip_file_name = 'cities15000.zip'
    cities_file_name = 'cities15000.txt'
    download_file('http://download.geonames.org/export/dump/cities15000.zip', cities_zip_file_name)
    unzip_file(cities_zip_file_name, os.getcwd())
    shutil.copy(cities_file_name, get_city_data_path())
    os.remove(cities_zip_file_name)    
    os.remove(cities_file_name)

save_file()
save_zip()