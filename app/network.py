import math
import random

from app.behavior import State

# from app.behavior import Behavior, NodeBehavior, Context

fruits = ["Abricot", "Amande", "Ananas", "Avocat", "Banane", "Cassis", "Cerise", "Citron", "Clémentine", "Coing", "Datte", "Figue", "Fraise", "Framboise", "Fruit de la passion", "Grenade", "Groseille", "Kaki", "Kiwi", "Kumquat", "Litchi", "Mandarine", "Mangue", "Marron", "Melon", "Mirabelle", "Mûre", "Myrtille", "Nectarine", "Noisette", "Noix", "Orange", "Pamplemousse", "Papaye", "Pastèque", "Pêche", "Poire", "Pomme", "Prune", "Quetsche", "Raisin", "Reine-claude", "Tomate"]  # noqa
random.shuffle(fruits)


class Point(object):
    """ Point class represents and manipulates x, y coords. """

    def __init__(self, x=0, y=0):
        """Create a new point with x and y, by default 0, 0"""
        self.x = x
        self.y = y

    def __str__(self):
        return "Point ({}, {})".format(str(self.x), str(self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def polar_coord_to(self, position):
        distance = self.distance_to(position)
        return {
            'angle': self.angle_with(position, distance),
            'distance': distance
        }

    def distance_to(self, point):
        sq_dist_x = (self.x - point.x) ** 2
        sq_dist_y = (self.y - point.y) ** 2
        return math.sqrt(sq_dist_x + sq_dist_y)

    def angle_with(self, point, distance=None):
        # Using this formula cos(a) = opp/hyp
        opposite = self.y - point.y
        hypot = self.distance_to(point) if distance is None else distance
        if (opposite == 0):
            return 0 if self.x < point.x else 180
        elif (hypot == 0):  # not tested
            return 0
        angle = math.degrees(math.acos(opposite / hypot))
        # Enables full circle angles
        angle = angle if point.x < self.x else 360 - angle
        return (angle + 90) % 360  # rotation needed, since normal is facing up

    def outbound(self, pt_a, pt_b):
        return (self.x < min(pt_a.x, pt_b.x) or self.x > max(pt_a.x, pt_b.x) or
                self.y < min(pt_a.y, pt_b.y) or self.y > max(pt_a.y, pt_b.y))

    def closer_than(self, other, pt):
        return other is None or (self.distance_to(pt) <= other.distance_to(pt))


class Line(object):

    def __init__(self, pt=[0, 0], vector=[0, 0]):
        self.pt = pt
        self.vector = vector

    def get_y(self, x):
        return (self.vector[1] / self.vector[0]) * (x - self.pt.x) + self.pt.y

    def get_x(self, y):
        return self.pt.x - (self.vector[0] / self.vector[1]) * (self.pt.y - y)

    def get_perpendicular(self, pt):
        return Line(pt, [self.vector[1], - self.vector[0]])

    def get_intersection_point(self, line):
        pt_a = self.pt
        a = self.vector[0]
        b = self.vector[1]

        pt_b = line.pt
        u = line.vector[0]
        v = line.vector[1]

        if a == 0:
            return Point(pt_a.x, pt_b.y)

        part_result = pt_b.y - pt_a.y + (b / a) * (pt_a.x - pt_b.x)
        lb = part_result * (a / (b * u - a * v))

        return Point(
            pt_b.x + lb * u,
            pt_b.y + lb * v)


class NetworkElem(object):
    def __init__(self):
        pass

    def __eq__(self, other):
        return (type(self) == type(other) and (
            self.eq(other)))


class Node(Point, NetworkElem):

    base_x = 25
    base_y = 25

    def __init__(self, x, y, name=None):
        if name is None:
            name = fruits.pop(0)
            fruits.append(name)
        self.name = name
        super().__init__(Node.base_x * x, Node.base_y * y)

    def __eq__(self, other):
        return type(self) == type(other) and (
            self.x == other.x and self.y == other.y)

    def __str__(self):
        return "Node ({}, {})".format(self.x, self.y)

    def __hash__(self):  # not tested
        return hash(self.__key())

    def __key(self):  # not tested
        return tuple(v for k, v in sorted(self.__dict__.items()))


class Link(Line, NetworkElem):

    def __init__(self, a, b, name=None):
        self.name = name
        if a.x < b.x or (a.x == b.x) and (a.y < b.y):
            (self.first, self.sec) = (a, b)
        else:
            (self.first, self.sec) = (b, a)

        vector = [self.sec.x - self.first.x, self.sec.y - self.first.y]
        super().__init__(self.first, vector)

    def __eq__(self, other):
        return type(self) == type(other) and (
            self.first == other.first and self.sec == other.sec)

    def __str__(self):
        return self.name if self.name is not None else\
            str(self.first) + " " + str(self.sec)

    def polar_coord_to(self, point):
        perpendicular = self.get_perpendicular(point)
        closest_pt = self.get_intersection_point(perpendicular)
        if closest_pt.outbound(self.first, self.sec):
            dist_w_first = point.distance_to(self.first)
            dist_w_sec = point.distance_to(self.sec)
            closest_pt = self.first if dist_w_first <= dist_w_sec else self.sec
        return closest_pt.polar_coord_to(point)

    def distance_to(self, point):
        perpendicular = self.get_perpendicular(point)
        closest_pt = self.get_intersection_point(perpendicular)
        if closest_pt.outbound(self.first, self.sec):
            dist_w_first = point.distance_to(self.first)
            dist_w_sec = point.distance_to(self.sec)
            closest_pt = self.first if dist_w_first <= dist_w_sec else self.sec
        return closest_pt.distance_to(point)

    def directions(self, point):
        directions = []
        if point.distance_to(self.first) > 10:
            directions.append(self.first.angle_with(self.sec))
        if point.distance_to(self.sec) > 10:
            directions.append(self.sec.angle_with(self.first))
        return directions

    def closer_than(self, other, pt):
        return other is None or (self.distance_to(pt) <= other.distance_to(pt))


class Network(object):

    def __init__(self, nodes=[], links=[]):
        self.nodes = nodes
        self.links = links

    def __str__(self):
        description = "Network:\n"
        for link in self.links:
            description += str(link) + ',\n'
        return description[:-2]

    @staticmethod
    def generate(nb_connections=0):
        if nb_connections > 7:
            raise Exception("Not possible with a center node")
        possibilities = [
            Node(10, 7), Node(12, 8),
            Node(13, 10), Node(12, 12),
            Node(10, 13), Node(8, 12),
            Node(7, 10), Node(8, 8)
        ]
        random.shuffle(possibilities)
        nodes = [Node(10, 10)]
        links = []
        while nb_connections > 0:
            nodes.append(possibilities.pop())
            links.append(Link(nodes[0], nodes[-1]))
            nb_connections -= 1
        return Network(nodes, links)

    def what_under(self, pos):
        node_under = next((nd for nd in self.nodes if State.which(
            nd.distance_to(pos)) == State.on), None)
        if node_under:
            return node_under
        link_under = next((lk for lk in self.links if State.which(
            lk.distance_to(pos)) == State.on), None)
        return link_under

    def start_node(self):
        start_node = None
        for node in self.nodes:
            if start_node is None or node.y > start_node.y:
                start_node = node
        return start_node

    def connected_nodes_to(self, node):
        connected_nodes = {}
        for link in self.links:
            if link.first == node:
                angle = int(node.angle_with(link.sec))
                connected_nodes[angle] = link.sec
            elif link.sec == node:
                angle = int(node.angle_with(link.first))
                connected_nodes[angle] = link.first
        return connected_nodes

    def node_in_direction(self, origin, to):
        if to in self.connected_nodes_to(origin):
            return self.connected_nodes_to(origin)[to]
        else:
            return None
