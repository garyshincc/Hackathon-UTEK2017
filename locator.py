import json
from haversine import *
import operator
from operator import itemgetter

lat_from = raw_input('give us your latitude: ')

lon_from = raw_input('give us your longitude: ')
lat_from = float(lat_from)
lon_from = float(lon_from)
with open('charging_stations.json') as data_file:    
    data = json.load(data_file)

list_of_closest = []

longest_distance = 100000

it = 0

for value in data.values()[1]:
	address = value['street_address']
	lon = value['longitude']
	lat = value['latitude']

	distance = haversine(lat_from, lon_from, lat, lon)
	print distance
	if distance < longest_distance:
		print str(distance) + " is shorter than " + str(longest_distance)
		location = {
			'address':address,
			'longitude':lon,
			'latitude':lat,
			'distance':distance,
		}
		list_of_closest.append(location)
		list_of_closest = sorted(list_of_closest, key = itemgetter('distance'))
		if len(list_of_closest) > 3:
			list_of_closest = list_of_closest[:3]
			
		if len(list_of_closest) != 0:
			longest_distance = distance

for close in list_of_closest:
	print close









