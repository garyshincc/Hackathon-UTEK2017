from jsonparser import *
from graph import *
import sys

us_map = Map()


list_of_charging_stations = jsonparser()


lat_from = raw_input('give us your latitude: ')

lon_from = raw_input('give us your longitude: ')
lat_from = float(lat_from)
lon_from = float(lon_from)

for charging_station in list_of_charging_stations:
	lat_to = charging_station['latitude']
	lon_to = charging_station['longitude']
	distance = haversine(lat_from, lon_from, lat_to, lon_to)
	station_name = charging_station['station_name']
	city = charging_station['city']
	_id = chargin_station['id']

	us_map.add_c_s(distance, station_name, _id, city, lat_to,lon_to)

for cs in us_map:
	pass

def make_graph(lat_from, long_from, lat_to, long_to):

	distance = haversine(lat_from, long_from, lat_to, long_to)

	if (distance < 480):
		pass
		# Do an api call

	else:
		pass #Use Dijkstra to find all charging points within range

def shortestPath():
	pass


































