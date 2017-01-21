import sys

class Charging_Station:
    def __init__(self, node_id, station_name, station_id, city, lat, long):
        self.node_id = node_id
        self.station_name = station_name
        self.station_id = station_id
        self.city = city
        self.lat = lat
        self.long = long

        # for pathfinding

        self.previous = None
        self.distance = sys.maxint
        self.adjacent = {}

    def __str__(self):
        return str(self.station_name) + " at " + str(self.city)


    def add_connection(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self, _id):
        return self.adjacent[_id]

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

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Map:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_c_s(self, node):
        self.num_vertices = self.num_vertices + 1
        new_c_s = Charging_Station(node)
        self.vert_dict[node] = new_c_s
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

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous
