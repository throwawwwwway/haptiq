import math
import conf


class NetworkBehavior(object):

    def __init__(self, behaviors=[]):
        self.behaviors = behaviors
        conf.logger.info('NetworkBehavior created')

    def trigger_on(self, raw):
        conf.logger.info('NetworkBehavior triggered')
        for behavior in self.behaviors:
            if behavior.is_valid(raw.get_state()):
                behavior.trigger_on(raw)


class Behavior(object):
    def __init__(self, graph_elem, pattern, in_range):
        self.graph_elem = graph_elem
        self.pattern = pattern
        self.in_range = in_range
        conf.logger.info('Behavior created')

    def is_valid(self, device_state):
        position = device_state['position']
        distance = self.graph_elem.get_distance_from(position)
        is_valid = distance <= self.in_range
        conf.logger.debug('is valid: {}'.format(str(is_valid)))
        return is_valid

    def trigger_on(self, raw):
        conf.logger.info('Behavior triggered')
        level = self.pattern.next_level()
        for direction in self.graph_elem.orientations:
            raw.set_level_on_direction(direction, level)


class Link(object):

    def __init__(self, node, edon):
        self.node = node
        self.edon = edon
        self.orientation = 0

    def get_nodes(self):
        return [self.node, self.edon]


class Node(object):

    def __init__(self, point):
        self.point = point
        self.orientations = [0, 90, 180, 270]
        conf.logger.debug("Point created ({}, {})".format(point.x, point.y))

    def get_distance_from(self, point):
        sq_dist_x = (point.x - self.point.x) ** 2
        sq_dist_y = (point.y - self.point.y) ** 2
        distance = math.sqrt(sq_dist_x) + math.sqrt(sq_dist_y)
        conf.logger.debug("Distance is: {}".format(str(distance)))
        return distance
