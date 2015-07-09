import app.conf as cf

from app.network import Point


class Haptiq(object):

    def __init__(self, name, level):
        self.name = name
        self._level = level
        self._previous_level = None

    def __str__(self):
        return "{}: {}".format(self.name, str(self.level))

    def __gt__(self, other):
        return self._level > other._level

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if (not isinstance(level, int) and not isinstance(level, float)):
            raise Exception('level should be int or float')
        elif (level < 0 or level > 100):
            cf.logger.warning('level should be an int between 0 and 100')
            level = 0
        self._level = level

    def should_update(self):
        if self._previous_level != self.level:
            self._previous_level = self.level
            return True
        return False


class Actuator(Haptiq):
    """ Actuator class represents the different actuators of the HaptiQ. """
    default = 10

    def __init__(self, angle=None, name='actuator', level=0):
        self.angle = angle
        super().__init__(name, level)
        cf.logger.debug("Actuator {} for {}° created - {}".format(
            name, str(angle), str(level)))


class Button(Haptiq):

    def __init__(self, name='button', level=50):
        super().__init__(name, level)


class Raw(object):
    """
        Raw is the interface that will serve as an interpret with the HaptiQ.
    """

    def __init__(self, actuators=[], button=None):
        """
            Initialize a Raw interface with:
            actuautors at level 0
            angle facing North (90)
            position at (0, 0)
            isPressed at False
        """
        self.actuators = actuators
        self._orientation = 0
        self._position = Point(0, 0)
        self.mouse_moved = False
        self.isPressed = False
        self.button = button

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if value != self._position:
            # cf.logger.debug("position is now: {}".format(str(value)))
            self._position = value

    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, value):
        value = (value - 90) % 360  # north is the "normal orientation"
        if value != self.orientation:
            cf.logger.debug("orientation is now: {}".format(str(value)))
            # self._orientation = value

    def actuator_for_angle(self, angle):
        angle = (angle + 180 - self.orientation) % 360
        std_angle = self.actuators[1].angle - self.actuators[0].angle
        for actuator in self.actuators:
            if abs(angle - actuator.angle) <= (std_angle / 2):
                return actuator
        return self.actuators[0]  # angle must be near 360 -> East

    def set_all_at(self, level):
        for actuator in self.actuators:
            actuator.level = level

    def reset_actuators(self):
        self.set_all_at(Actuator.default)
