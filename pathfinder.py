from jsonparser.py import *

def makeGraph(lat_from, long_from, lat_to, long_to):
	distance = haversine(lat_from, long_from, lat_to, long_to)

	if (distance < 480):
		# Do an api call

	else:
		#Use Dijkstra to find all charging points within range

def shortestPath():
