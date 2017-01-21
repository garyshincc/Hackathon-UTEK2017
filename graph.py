import sys
from haversine import *

class Charging_Station:
    def __init__(self, station_name, station_id, city, lat, lon):
        self.station_name = station_name
        self.station_id = station_id
        self.city = city
        self.lat = lat
        self.lon = lon

        # for pathfinding

        self.previous = None
        self.distance = sys.maxint
        self.adjacent = {}

    def __str__(self):
        return str(self.station_name) + " at " + str(self.city)


    def add_connection(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self, station_id):
        return self.adjacent[station_id]

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def get_latitude(self):
        return float(self.lat)

    def get_longitude(self):
        return float(self.lon)

    def __str__(self):
        return str(self.station_id) + ' adjacent: ' + str([x.station_id for x in self.adjacent])

class Map:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __str__(self):
        mystr = ''
        for cs in self.vert_dict:
            mystr + str(cs)
        return mystr

    def __iter__(self):
        return iter(self.vert_dict.values())

    def cost(self, current, next):
        current = self.get_c_s(current)
        next = self.get_c_s(next)
        return haversine(current.get_latitude(), current.get_longitude(), next.get_latitude(), next.get_longitude())

    def add_c_s(self, station_name, station_id, city, lat, long):
        self.num_vertices = self.num_vertices + 1
        new_c_s = Charging_Station(station_name, station_id, city, lat, long)
        self.vert_dict[station_id] = new_c_s
        return new_c_s

    def get_c_s(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_c_s(frm)
        if to not in self.vert_dict:
            self.add_c_s(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self, current):
        return self.vert_dict

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous
