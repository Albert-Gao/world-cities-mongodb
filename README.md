# world-cities-database

The data is from [GeoNames](http://www.geonames.org/). It will save 2 collections to your mongodb, one is the cities and one is the countries. Very easy to use and easy to update.

## Python version

- Python 3
- Python 2 should be fine, but haven't tried.

## How to use

1. `git clone https://github.com/Mr-Binary/world-cities-mongodb.git`

1. `pip install pymongo`

1. Open `settings.py`, set up your database settings.

1. `python main.py`

1. Enjoy :)

## Structure

-- `[data]`: [Folder] Raw data from GeoNames
-- `[models]`: [Folder] database model for city and country
-- `[utils]`: [Folder] Helper function
-- `settings.py`: Settings
-- `main.py`: Main file

## About the data
The `cities` contains cities which population greater than 15000.

To update the data, you just need to download them from GeoNames:
- [cities15000.zip](http://download.geonames.org/export/dump/cities15000.zip)
- [countryInfo.txt](http://download.geonames.org/export/dump/countryInfo.txt)

And update the according file in `data` folder.

## Tips

1. Every execution will drop the previous collection and generate new one.

2. How about support other database? I think it could, you just need to refactor the `save_cities()` and `save_countries()` in `mongodb.py`, then it will be called at run time with the list of data to insert.
