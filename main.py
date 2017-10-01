from utils.mongodb import init, save_cities, save_countries
from utils.parser import parse_city, parse_country

init()

parse_city()
parse_country()

save_cities()
save_countries()
