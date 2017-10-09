from settings import COUNTRY_FIELDS_BLACKLIST
from data.CurrencySymbols import CURRENCY_SYMBOLS
from utils.util import remove_field_from_blacklist

COUNTRY_FIELDS = {
    'ISO': 0, # ISO
    'ISO3': 1, # ISO3
    'ISO_Numeric': 2, # ISO-Numeric
    'fips': 3, # fips
    'Country' : 4, # Country
    'Capital': 5, # Capital
    'Area': 6, 	# Area(in sq km)
    'Population': 7, # Population
    'Continent': 8, # Continent
    'tld': 9, # tld
    'Currency_Code': 10, # CurrencyCode
    'Currency_Name': 11, # CurrencyName
    'Phone': 12, # Phone
    'Postal_Code_Format': 13, # Postal Code Format
    'Postal_Code_Regex': 14, # Postal Code Regex
    'Languages': 15, # Languages
    'country_id': 16, # geonameid
    'neighbours': 17, # neighbours
    'Equivalent_Fips_Code': 18 # EquivalentFipsCode
}

class Country(object):
    def __init__(self, data):
        super(Country, self).__init__()

        if not isinstance(data, list):
            raise ValueError("Expect data to be a list")

        self.iso = data[COUNTRY_FIELDS['ISO']]
        self.iso3 = data[COUNTRY_FIELDS['ISO3']]
        self.iso_numeric = int(data[COUNTRY_FIELDS['ISO_Numeric']])
        self.fips = data[COUNTRY_FIELDS['fips']]
        self.country = data[COUNTRY_FIELDS['Country']]
        self.capital = data[COUNTRY_FIELDS['Capital']]
        self.area = data[COUNTRY_FIELDS['Area']]
        self.population = int(data[COUNTRY_FIELDS['Population']])
        self.continent = data[COUNTRY_FIELDS['Continent']]
        self.tld = data[COUNTRY_FIELDS['tld']]
        self.currency_code = data[COUNTRY_FIELDS['Currency_Code']]
        self.currency_name = data[COUNTRY_FIELDS['Currency_Name']]
        self.currency_symbol = self.get_currency_symbol()
        self.phone = data[COUNTRY_FIELDS['Phone']]
        self.postal_code_format = data[COUNTRY_FIELDS['Postal_Code_Format']]
        self.postal_code_regex = data[COUNTRY_FIELDS['Postal_Code_Regex']]
        self.languages = data[COUNTRY_FIELDS['Languages']].split(',')
        self.country_id = int(data[COUNTRY_FIELDS['country_id']])
        self.neighbours = data[COUNTRY_FIELDS['neighbours']].split(',')
        self.equivalent_fips_code = data[COUNTRY_FIELDS['Equivalent_Fips_Code']]

    def get_currency_symbol(self):
        if not self.currency_code:
            return ''

        if self.currency_code in CURRENCY_SYMBOLS.keys():
            return CURRENCY_SYMBOLS[self.currency_code]
        else:
            return ''

    def to_dict(self):
        return remove_field_from_blacklist(COUNTRY_FIELDS_BLACKLIST, self.__dict__)
