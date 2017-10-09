from settings import CITY_FIELDS_BLACKLIST
from utils.util import remove_field_from_blacklist

CITY_FIELDS = {
    'city_id': 0, # integer id of record in geonames database
    'name': 1, # name of geographical point (utf8) varchar(200)
    'ascii_name': 2, # name of geographical point in plain ascii characters, varchar(200)
    'alternate_names': 3, # alternatenames, comma separated, ascii names automatically transliterated, convenience attribute from alternatename table, varchar(10000)
    'latitude': 4, #latitude in decimal degrees (wgs84)
    'longitude': 5, # longitude in decimal degrees (wgs84)
    'feature_class': 6, # see http://www.geonames.org/export/codes.html, char(1)
    'feature_code': 7, # see http://www.geonames.org/export/codes.html, varchar(10)
    'country_code': 8, # ISO-3166 2-letter country code, 2 characters
    'cc2': 9, # alternate country codes, comma separated, ISO-3166 2-letter country code, 200 characters
    'admin1_code': 10, # fipscode (subject to change to iso code), see exceptions below, see file admin1Codes.txt for display names of this code; varchar(20)
    'admin2_code': 11, # code for the second administrative division, a county in the US, see file admin2Codes.txt; varchar(80)
    'admin3_code': 12, # code for third level administrative division, varchar(20)
    'admin4_code': 13, # code for fourth level administrative division, varchar(20)
    'population': 14, # bigint (8 byte int)
    'elevation': 15, # in meters, integer
    'dem': 16, # digital elevation model, srtm3 or gtopo30, average elevation of 3''x3'' (ca 90mx90m) or 30''x30'' (ca 900mx900m) area in meters, integer. srtm processed by cgiar/ciat.
    'timezone': 17, # the iana timezone id (see file timeZone.txt) varchar(40)
    'modification_date': 18, # date of last modification in yyyy-MM-dd format
}

class City(object):
    def __init__(self, data):
        super(City, self).__init__()

        if not isinstance(data, list):
            raise ValueError("Expect data to be a list")

        self.city_id = int(data[CITY_FIELDS['city_id']])
        self.name = data[CITY_FIELDS['name']]
        self.ascii_name = data[CITY_FIELDS['ascii_name']]
        self.alternate_names = data[CITY_FIELDS['alternate_names']].split(',')
        self.latitude = data[CITY_FIELDS['latitude']]
        self.longitude = data[CITY_FIELDS['longitude']]
        self.feature_class = data[CITY_FIELDS['feature_class']]
        self.feature_code = data[CITY_FIELDS['feature_code']]
        self.country_code = data[CITY_FIELDS['country_code']]
        self.cc2 = data[CITY_FIELDS['cc2']]
        self.admin1_code = data[CITY_FIELDS['admin1_code']]
        self.admin2_code = data[CITY_FIELDS['admin2_code']]
        self.admin3_code = data[CITY_FIELDS['admin3_code']]
        self.admin4_code = data[CITY_FIELDS['admin4_code']]
        self.population = int(data[CITY_FIELDS['population']])
        self.elevation = data[CITY_FIELDS['elevation']]
        self.dem = data[CITY_FIELDS['dem']]
        self.timezone = data[CITY_FIELDS['timezone']]
        self.modification_date = data[CITY_FIELDS['modification_date']]

    def to_dict(self):
        return remove_field_from_blacklist(CITY_FIELDS_BLACKLIST, self.__dict__)
