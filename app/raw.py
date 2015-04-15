import conf as cf


class Point(object):
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """Create a new point with x and y, by default 0, 0"""
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(str(self.x), str(self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Actuator(object):
    """ Actuator class represents the different actuators of the HaptiQ. """

    def __init__(self, angle, name='unknwon'):
        self.angle = angle
        self.name = name

        cf.logger.debug(
            "Actuator {} for {}° created".format(name, str(angle)))

    def __str__(self):
        return self.name


class Raw(object):
    """
        Raw is the interface that will communicate with the HaptiQ.
    """
    ON_NODE = 20
    OUTRANGE_NODE = 100
    CODED_LEVEL_LIMIT = 75

    def __init__(self, actuators=[]):
        """
            Initialize a Raw interface with:
            actuautors at level 0
            angle facing North (90)
            position at (0, 0)
            isPressed at False
        """
        self.actuators = actuators
        self.angle = 90  # North
        self.position = Point(0, 0)
        self.isPressed = False
        self.levels = {}
        for actuator in actuators:
            self.levels[actuator] = 0

    def get_level(self, actuator):
        """Get the level of the designated actuator"""
        if (actuator in self.actuators):
            return self.levels[actuator]
        else:
            raise Exception('Actuator does not exist')

    def set_level(self, actuator, level):
        """
            Set the level of the designated actuator

            Raises exception if:
            * actuator is not in self.actuators
            * level is not an integer
            * level is not between 0 and 100
        """
        if (actuator in self.actuators):
            if (not isinstance(level, int) and not isinstance(level, float)):
                raise Exception('level should be int or float')
            elif (level < 0 or level > 100):
                raise Exception('level should be an int between 0 and 100')
            self.levels[actuator] = level
        else:
            raise Exception('Actuator does not exist')

    def get_state(self):
        """Returns the current state of the HaptiQ"""
        return {
            'position': self.position,
            'angle': self.angle
        }

    def get_actuators_interval(self, angle):
        angle = angle % 360
        lw_actuator = None
        lw_min_delta = 360
        # for everything near and below 360
        hi_actuator = self.actuators[0]
        hi_min_delta = 360
        cf.logger.debug("Looking for actuator")
        for actuator in self.actuators:
            delta = angle - actuator.angle
            if (delta >= 0 and delta < lw_min_delta):
                lw_actuator = actuator
                lw_min_delta = delta
            delta = actuator.angle - angle
            if (delta >= 0 and delta < hi_min_delta):
                hi_actuator = actuator
                hi_min_delta = delta
        if lw_actuator == hi_actuator:
            return [lw_actuator]
        else:
            return [lw_actuator, hi_actuator]

    def get_levels_for_coding(self, angle, distance):
        """ Returns levels from 0 to CODED_LEVEL_LIMIT with their actuators """
        # import pdb; pdb.set_trace()
        if (distance > Raw.OUTRANGE_NODE):
            return {}
        angle = (angle + 180) % 360
        interval = self.get_actuators_interval(angle)
        limit = Raw.CODED_LEVEL_LIMIT
        coded_level = (Raw.OUTRANGE_NODE - distance) * limit / Raw.OUTRANGE_NODE

        if len(interval) == 1:
            return {interval[0]: coded_level}
        else:
            actuators_marge = (interval[1].angle - interval[0].angle) % 360
            ratio = (angle - interval[0].angle) / actuators_marge
            return {
                interval[0]: (1. - ratio) * coded_level,
                interval[1]: ratio * coded_level
            }

    def set_all_at(self, level):
        for actuator in self.actuators:
            self.set_level(actuator, level)
