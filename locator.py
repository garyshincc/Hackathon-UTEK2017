import json
from haversine import *
import operator
from operator import itemgetter

def locator(lat_from, lon_from):
	with open('charging_stations.json') as data_file:    
	    data = json.load(data_file)

	list_of_closest = []

	longest_distance = 100000

	it = 0

	for value in data.values()[1]:
		address = value['station_name']
		lon = value['longitude']
		lat = value['latitude']
		station_id = value['id']


		distance = haversine(lat_from, lon_from, lat, lon)
		if distance < longest_distance:
			location = {
				'station_name':address,
				'longitude':lon,
				'latitude':lat,
				'distance':distance,
				'station_id':station_id,
			}
			list_of_closest.append(location)
			new_list = sorted(list_of_closest, key = itemgetter('distance'))
			list_of_closest = new_list
			if len(list_of_closest) > 3:
				list_of_closest = list_of_closest[:3]
				
			if len(list_of_closest) != 0:
				longest_distance = list_of_closest[len(list_of_closest) -1]['distance'] 

	print "I've found 3 closest charging stations near you: "
	for close in list_of_closest[:3]:
		print str(close['latitude']) + ' ' + str(close['longitude']) + ' ' + str(close['station_name']) + ' ' + str(close['distance'])

	return list_of_closest












