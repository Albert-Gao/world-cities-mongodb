from utils.mongodb import init, save_cities, save_countries
from utils.parser import parse_city, parse_country, remove_non_match_language_countries_and_cities

init()

parse_city()
parse_country()

remove_non_match_language_countries_and_cities()

save_cities()
save_countries()
