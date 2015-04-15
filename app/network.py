import math
import conf as cf

from raw import Point


class Network(object):
    ON_NODE = 15
    NEAR_NODE = 100

    def __init__(self, nodes=[], links=[], raw=None):
        self.nodes = nodes
        self.links = links
        self.raw = raw

    def trigger_behavior(self):
        cur_state = self.raw.get_state()
        coded_levels = {}
        for node in self.nodes:
            distance = node.get_distance_to(cur_state['position'])
            angle = node.get_angle_with(cur_state['position'])
            cf.logger.info("Distance: {}, Angle: {}°".format(distance, angle))
            if (distance <= Network.ON_NODE):
                self.raw.set_all_at(100)
                break
            self.raw.set_all_at(0)
            if (distance <= Network.NEAR_NODE):
                #  will indicate the orientation
                coded_levels = self.raw.get_levels_for_coding(angle, distance)
            for actuator in coded_levels:
                self.raw.set_level(actuator, coded_levels[actuator])


class Link(object):

    def __init__(self, node, edon):
        self.node = node
        self.edon = edon


class Node(object):

    def __init__(self, x, y):
        self.point = Point(x, y)
        cf.logger.debug("Point created ({}, {})".format(x, y))

    def get_distance_to(self, point):
        sq_dist_x = (self.point.x - point.x) ** 2
        sq_dist_y = (self.point.y - point.y) ** 2
        return math.sqrt(sq_dist_x + sq_dist_y)

    def get_angle_with(self, point):
        # Using this formula cos(a) = opp/hyp
        opposite = self.point.y - point.y
        hypotenuse = self.get_distance_to(point)
        if (opposite == 0 or hypotenuse == 0):
            return 0
        angle = math.degrees(math.acos(opposite / hypotenuse))
        # Enable full circle angles
        angle = angle if point.x < self.point.x else 360 - angle
        return (angle + 90) % 360  # rotation needed
