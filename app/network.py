import math

# from app.behavior import Behavior, NodeBehavior, Context


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


class Node(Point, NetworkElem):

    base_x = 25
    base_y = 25

    def __init__(self, x, y):
        super().__init__(Node.base_x * x, Node.base_y * y)

    def __str__(self):
        return "Node ({}, {})".format(self.x, self.y)

    def __hash__(self):  # not tested
        return hash(self.__key())

    def __key(self):  # not tested
        return tuple(v for k, v in sorted(self.__dict__.items()))


class Link(Line, NetworkElem):

    def __init__(self, a, b, name=None):
        self.name = name
        (self.first, self.sec) = (a, b) if a.x <= b.x else (b, a)

        vector = [self.sec.x - self.first.x, self.sec.y - self.first.y]
        super().__init__(self.first, vector)

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

    def directions(self, point):
        directions = []
        if point.distance_to(self.first) > 10:
            directions.append(self.first.angle_with(self.sec))
        if point.distance_to(self.sec) > 10:
            directions.append(self.sec.angle_with(self.first))
        return directions


class Network(object):

    def __init__(self, nodes=[], links=[]):
        self.elems = nodes + links
        # self.elems = {e: (e.default_behavior(), []) for e in nodes + links}

    def distances(self, point):
        return {elem: elem.polar_coord_to(point) for elem in self.elems}
    # def apply_behaviors(self):
    #     """
    #         Apply for each network element the set behavior
    #         to corresponding the actuators
    #     """

    #     self.raw.reset_actuators()
    #     for (behavior, actuators) in self.elems.values():
    #         behavior.apply(actuators)
    #     Behavior._iter += 1  # for syncing behavior

    # def update_behaviors(self):
    #     """Update the behaviors"""

    #     sorted_keys = sorted(
    #         self.elems,
    #         key=lambda e: e.polar_coord_to(self.raw.position)['distance']
    #     )

    #     for elem in sorted_keys:
    #         coord = elem.polar_coord_to(self.raw.position)
    #         context = Context.which(coord['distance'])

    #         (behavior, actuators) = self.elems[elem]
    #         if context == Context.on:
    #             if type(elem) == Node:
    #                 actuators = self.raw.actuators
    #             else:
    #                 actuators = [
    #                     self.raw.actuator_for_angle(direction)
    #                     for direction in elem.directions(self.raw.position)
    #                 ]
    #         else:
    #             actuators = [self.raw.actuator_for_angle(coord['angle'])]
    #         behavior.update(context)
    #         self.elems[elem] = (behavior, actuators)
