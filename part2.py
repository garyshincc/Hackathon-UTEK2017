import requests
import json
from pprint import pprint


lat_from = raw_input('give us your latitude: ')
lon_from = raw_input('give us your longitude: ')
lat_to = raw_input('give us destination latitude: ')
lon_to = raw_input('give us destination longitude: ')
lat_from = float(lat_from)
lon_from = float(lon_from)
lat_to = float(lat_to)
lon_to = float(lon_to)

origin = str(lat_from) + ',' + str(lon_from)
destination = str(lat_to) + ',' + str(lon_to)

request = requests.get('https://maps.googleapis.com/maps/api/directions/json?origin=' + origin + '&destination=' + destination + '&key=AIzaSyCIREhnJrzCccqOx207RneuoA-IyhlzMi8')
jfile = request.content
j = json.loads(jfile)

for value in j.values()[0]:
	lat_long = value['bounds']
	distance = value['legs'][0]['distance']['value']
	duration = value['legs'][0]['duration']['value']
	print "distance: " + str(round(distance/1000.0,2)) + " km(s)"
	print "time: " + str(round(duration/3600.0,2)) + " hour(s)"









