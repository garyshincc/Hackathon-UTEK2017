from jsonparser import *
from graph import *

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
	_id = charging_station['id']

	us_map.add_c_s(distance, station_name, _id, city, lat_to,lon_to)

for c_s1 in us_map:
	for c_s2 in us_map:
		dist = haversine(c_s1['latitude'], c_s1['longitude'], c_s2['latitude'], c_s2['longitude'])
		if ((dist > 0) and (dist < 450)):
			us_map.add_connection(c_s2)
		

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

		for next in graph.neighbors(current):
			new_cost = cost_so_far[current] + graph.cost(current, next)
			if next not in cost_so_far or new_cost < cost_so_far[next]:
				cost_so_far[next] = new_cost
				priority = new_cost + heuristic(goal, next)
				frontier.put(next, priority)
				came_from[next] = current
	return came_from, cost_so_far




























