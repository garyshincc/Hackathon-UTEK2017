from jsonparser import *
from graph import *
from locator import *
from priority_queue import *
from pprint import pprint

us_map = Map()


list_of_charging_stations = jsonparser()


lat_from = raw_input('give us your latitude: ')
lon_from = raw_input('give us your longitude: ')
lat_to = raw_input('give us destination latitude: ')
lon_to = raw_input('give us destination longitude: ')
lat_from = float(lat_from)
lon_from = float(lon_from)
lat_to = float(lat_to)
lon_to = float(lon_to)

for charging_station in list_of_charging_stations:
	lat_to = charging_station['latitude']
	lon_to = charging_station['longitude']
	distance = haversine(lat_from, lon_from, lat_to, lon_to)
	station_name = charging_station['station_name']
	city = charging_station['city']
	_id = charging_station['id']

	us_map.add_c_s(station_name, _id, city, lat_to,lon_to)

for c_s1 in us_map:
	for c_s2 in us_map:
		dist = haversine(c_s1.get_latitude(), c_s1.get_longitude(), c_s2.get_latitude(), c_s2.get_longitude())
		if ((dist > 0) and (dist < 450)):
			c_s1.add_connection(c_s2)
		

def heuristic(lat_from, lon_from, lat_to, lon_to):
	return haversine (lat_from, lon_from, lat_to, lon_to)

def A_star_search(us_map, start, goal):
	frontier = PriorityQueue()
	frontier.put(start, 0)
	came_from = {}
	cost_so_far = {}
	came_from[start] = None
	cost_so_far[start] = 0
	while not frontier.empty():
		current = frontier.get()
		if current == goal:
			break

		for next in us_map.get_vertices(current):
			new_cost = cost_so_far[current] + us_map.cost(current, next)
			if next not in cost_so_far or new_cost < cost_so_far[next]:
				cost_so_far[next] = new_cost
				priority = new_cost + heuristic(us_map.get_c_s(goal).get_latitude(),us_map.get_c_s(goal).get_longitude(), us_map.get_c_s(next).get_latitude(),us_map.get_c_s(next).get_longitude())
				frontier.put(next, priority)
				came_from[next] = current
	return came_from, cost_so_far

closest_starting_station = locator(lat_from, lon_from)[0]

startlon = closest_starting_station['longitude']
startlat = closest_starting_station['latitude']
startid = closest_starting_station['station_id']

closes_ending_station = locator(lat_to, lon_to)[0]

endid = closes_ending_station['station_id']

path, distance = A_star_search(us_map, startid, endid)

print '\n\n'


pprint (path)
























