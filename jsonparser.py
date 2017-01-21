import json
from operator import itemgetter
from haversine import *


def jsonparser():
	list_of_dicts = []
	with open('charging_stations.json') as data_file:    
	    data = json.load(data_file)

	for value in data.values()[1]:

		address = value['station_name']
		lon = value['longitude']
		lat = value['latitude']
		city = value['city']
		id = value['id']

		my_dict = {
		'station_name': address,
		'latitude': lat,
		'longitude': lon,
		'city': city,
		'id': id,
		}

		list_of_dicts.append(my_dict)
		
	return list_of_dicts

