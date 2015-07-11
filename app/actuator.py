import app.logconfig as lc


class Actuator(object):
    """ Actuator class represents the different actuators of the HaptiQ. """

    def __init__(self, name="actuator", angle=None):
        self.name = name
        self.angle = angle
        self._level = 0
        lc.log.debug("Actuator {} for {} deg created - {}".format(
            name, str(self.angle), str(self.level)))

    def __str__(self):
        return "{}: {}".format(self.name, str(self.level))

    def __gt__(self, other):
        return self._level > other._level

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if not isinstance(level, int) and not isinstance(level, float):
            raise Exception("level must be int or float")
        elif level < 0 or level > 99:
            lc.log.warning("level must be between 0 and 99: {}".format(
                str(level)))
            level = 0
        self._level = level

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, angle):
        if not isinstance(angle, int) and not isinstance(angle, float):
            raise Exception("angle should be int or float")
        angle = angle % 360
        self._angle = angle


class Button(Actuator):
    """ A particular actuator, could be used for inputs. """
    def __init__(self, name='button'):
        super().__init__(name)
