import math
import app.conf as cf

from app.behavior import Behavior, NodeBehavior, LinkBehavior, Context


def which_context(distance):
    if (distance < 10):
        return Context.on
    elif (distance < 50):
        return Context.hot
    elif (distance < 100):
        return Context.cold
    return Context.outrange


class Network(object):

    def __init__(self, nodes=[], links=[], raw=None):
        self.raw = raw
        self.nodes_behavior = {}
        self.links_behavior = {}
        for node in nodes:
            self.nodes_behavior[node] = NodeBehavior()
        for link in links:
            self.links_behavior[link] = LinkBehavior()

    def apply_behaviors(self):
        """
            Apply the behavior for each node and link.
            The behavior can be an oscillation or a constant.
        """
        self.raw.set_all_at(Behavior.default)
        for node in self.nodes_behavior:
            self.nodes_behavior[node].apply()
        for link in self.links_behavior:
            self.links_behavior[link].apply()
        Behavior._iter += 1

    def update_behaviors(self):
        """Update the behaviors"""

        for node in list(self.nodes_behavior.keys()):
            coord = node.polar_coord_of(self.raw.position)
            context = which_context(coord['distance'])

            if (context == Context.on):
                actuators = self.raw.actuators
            else:
                actuators = [self.raw.actuator_for_angle(coord['angle'])]
            self.nodes_behavior[node].update_if_necessary(
                context, actuators, coord)

        for link in list(self.links_behavior.keys()):

            coord = link.closest_point_coord(self.raw.position)
            if coord is None:
                continue
            context = which_context(coord['distance'])

            if (context != Context.on):  # Get the direction towards link
                actuators = [
                    self.raw.actuator_for_angle(coord['angle'])
                ]
            else:   # Get the directions offered by the link
                actuators = [
                    self.raw.actuator_for_angle(direction)
                    for direction in link.directions(self.raw.position)
                ]

            self.links_behavior[link].update(context, actuators, coord)


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


class Link(Line):

    def __init__(self, a, b, name=None):
        self.name = name
        (self.first, self.sec) = (a, b) if a.x <= b.x else (b, a)

        vector = [self.sec.x - self.first.x, self.sec.y - self.first.y]
        super().__init__(self.first, vector)

    def __str__(self):
        return self.name if self.name is not None else\
            str(self.first) + " " + str(self.sec)

    def closest_point_coord(self, point):
        perpendicular = self.get_perpendicular(point)
        closest_pt = self.get_intersection_point(perpendicular)
        if closest_pt.outbound(self.first, self.sec):
            dist_w_first = point._distance_to(self.first)
            dist_w_sec = point._distance_to(self.sec)
            closest_pt = self.first if dist_w_first <= dist_w_sec else self.sec
        return closest_pt.polar_coord_of(point)

    def directions(self, point):
        directions = []
        if point._distance_to(self.first) > 10:
            directions.append(self.first._angle_with(self.sec))
        if point._distance_to(self.sec) > 10:
            directions.append(self.sec._angle_with(self.first))
        return directions


class Point(object):
    """ Point class represents and manipulates x, y coords. """

    def __init__(self, x=0, y=0):
        """Create a new point with x and y, by default 0, 0"""
        self.x = x
        self.y = y

    def __str__(self):
        return "POINT ({} {})".format(str(self.x), str(self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def polar_coord_of(self, position):
        distance = self._distance_to(position)
        return {
            'angle': self._angle_with(position, distance),
            'distance': distance
        }

    def _distance_to(self, point):
        sq_dist_x = (self.x - point.x) ** 2
        sq_dist_y = (self.y - point.y) ** 2
        return math.sqrt(sq_dist_x + sq_dist_y)

    def _angle_with(self, point, distance=None):
        # Using this formula cos(a) = opp/hyp
        opposite = self.y - point.y
        hypot = self._distance_to(point) if distance is None else distance
        if (opposite == 0):
            return 0 if self.x < point.x else 180
        elif (hypot == 0):  # not tested
            return 0
        angle = math.degrees(math.acos(opposite / hypot))
        # Enable full circle angles
        angle = angle if point.x < self.x else 360 - angle
        return (angle + 90) % 360  # rotation needed

    def outbound(self, pt_a, pt_b):
        return (self.x < min(pt_a.x, pt_b.x) or self.x > max(pt_a.x, pt_b.x) or
                self.y < min(pt_a.y, pt_b.y) or self.y > max(pt_a.y, pt_b.y))


class Node(Point):

    base_x = 25
    base_y = 25

    def __init__(self, x, y):
        super().__init__(Node.base_x * x, Node.base_y * y)

    def __str__(self):
        return "NODE ({} {})".format(self.x, self.y)

    def __hash__(self):  # not tested
        return hash(self.__key())

    def __key(self):  # not tested
        return tuple(v for k, v in sorted(self.__dict__.items()))
