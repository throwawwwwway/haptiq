import app.logconfig as lc

from app.network import Point


class Device(object):
    """Device represents the state of our HaptiQ."""

    def __init__(self, actuators=[]):
        """
            angle facing North (90)
            position at (0, 0)
        """
        self.actuators = actuators
        self._orientation = 0
        self._position = Point(0, 0)

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if value != self._position:
            # lc.log.debug("position is now: {}".format(str(value)))
            self._position = value

    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, value):
        # default orientation is north, calculation are based on easy -> 90°
        value = (value - 90) % 360
        if value != self.orientation:
            lc.log.debug("orientation is now: {}".format(str(value)))
            # TODO: self._orientation = value

    def actuators_for(self, graph_elem):
        directions = graph_elem.directions(self.position)
        return [self.actuator_for_angle(angle) for angle in directions]

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
        self.set_all_at(0)
