import conf as cf

from network import Point


class Actuator(object):
    """ Actuator class represents the different actuators of the HaptiQ. """

    def __init__(self, angle=None, name='unknwon', level=0):
        self.angle = angle
        self.name = name
        self._level = level

        cf.logger.debug("Actuator {} for {}° created - {}".format(
            name, str(angle), str(level)))

    def __str__(self):
        return "{}: {}".format(self.name, str(self.level))

    def __gt__(self, other):
        return self.level > other.level

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if (not isinstance(level, int) and not isinstance(level, float)):
            raise Exception('level should be int or float')
        elif (level < 0 or level > 100):
            cf.logger.warning('level should be an int between 0 and 100')
        self._level = level


class Raw(object):
    """
        Raw is the interface that will communicate with the HaptiQ.
    """

    def __init__(self, actuators=()):
        """
            Initialize a Raw interface with:
            actuautors at level 0
            angle facing North (90)
            position at (0, 0)
            isPressed at False
        """
        self.actuators = actuators
        self.angle = 90  # North
        self._position = Point(0, 0)
        self.mouse_moved = False
        self.isPressed = False

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self.mouse_moved = True
        self._position = value
        # if (value._distance_to(self._position) > 3):
        #     self.mouse_moved = True
        #     self._position = value
        # else:
        #     self.mouse_moved = False

    def actuator_for_angle(self, angle):
        angle = (angle + 180) % 360
        std_angle = self.actuators[1].angle - self.actuators[0].angle
        for actuator in self.actuators:
            if abs(angle - actuator.angle) <= (std_angle / 2):
                return actuator
        return self.actuators[0]  # angle must be near 360 -> East

    def get_interval_actuators_for_angle(self, angle):
        angle = (angle + 180) % 360
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

    def set_all_at(self, level):
        for actuator in self.actuators:
            actuator.level = level
