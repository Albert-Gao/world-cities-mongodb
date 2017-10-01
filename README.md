# world-cities-database

Do you want a database which contains most of cities in the world as well as the countries? This app will save 2 collections to your mongodb:

 1. `cities`(**23328** in total)
 1. `countries`(**252** in total)

## Why use

 - Language agnostic since it's not a lib. Consume the result database using any language you like.
 - No other 3rd party libs dependencies but official `pymongo`
 - `python main.py` to generate the database from source data
 - `python update.py` to update the source data from GeoNames
 - Remove any fields you don't need in `settings.py`
 - Support `currency symbol` which not included in the GeoNames (like `$` for `USD`)
 - Easy to add support for other database. See `FAQ` part.
 - Could add "duplicate" data to prevent join query (see `settings.py`)

## Python version

- Python 3
- Python 2 should be fine, but haven't tried.

## How to use

1. `git clone https://github.com/Mr-Binary/world-cities-mongodb.git`

1. `pip install pymongo`

1. Open `settings.py`, set up your database settings.

1. `python main.py`

1. Enjoy :)

- To update the source data in `data` folder: **`python update.py`**

## Folder Structure

- `[data]`: [Folder] Raw data from GeoNames
- `[models]`: [Folder] database model for city and country
- `[utils]`: [Folder] Helper function
- `settings.py`: Settings
- `main.py`: Main file to generate the database
- `update.py`: Update the source `data` from GeoNames

## About the data

- The data is from [GeoNames](http://www.geonames.org/).

- The `cities` contains cities which population greater than 15000.

- The foreign key to refer is `geo_name_id`

- How to update the data
  - **`python update.py`**

- The URL of source data from GeoNames:
  - [cities15000.zip](http://download.geonames.org/export/dump/cities15000.zip)
  - [countryInfo.txt](http://download.geonames.org/export/dump/countryInfo.txt)

## FAQ

### What will happen if I run the app twice

- Every execution will drop the previous collection and generate new one.

### How about support other database

- It's very easy, you just need to refactor the `save_cities()` and `save_countries()` in `mongodb.py`, then it will be called at run time with the list of data to insert.
