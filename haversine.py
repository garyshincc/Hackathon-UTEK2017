import math

def haversine(lat_from, long_from, lat_to, long_to):
	radius = 6371.0
	
	lat_from, long_from, lat_to, long_to = map(math.radians, [lat_from, long_from, lat_to, long_to])

	dlat = lat_from - lat_to
	dlon = long_from - long_to
	a = ( math.sin((dlat)/2.0)**2.0 ) + ( math.cos(lat_to)*math.cos(lat_from)*math.sin(dlon/2.0)**2.0 )
	arc = math.asin(math.sqrt(a))
	distance = 2 * radius * arc
	return distance
