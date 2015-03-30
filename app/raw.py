class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """Create a new point with x and y, by default 0, 0"""
        self.x = x
        self.y = y


class Raw(object):
    """
        Raw is the interface that will communicate with the HaptiQ.

        Attributes:
        actuators   -- a list of the actuators designation (string)
        orientation -- where the device is oriented (between 0 and 360)
        position    -- the last recorded position
        isPressed   -- the main input state

        Methods:
        get_level   -- get the level of the designated actuator
        set_level   -- set the level of the designated actuator, is must exist
        get_orientation
        set_orientation
        get_position
        set_position
        is_pressed
        set_pressed
    """

    def __init__(self, actuators=[]):
        """
            Initialize a Raw interface with:
            actuautors at level 0
            orientation facing North (90)
            position at (0, 0)
            isPressed at False
        """
        self.actuators = actuators
        self.orientation = 90  # North
        self.position = Point(0, 0)
        self.isPressed = False
        self.levels = {}
        for actuator in actuators:
            self.levels[actuator] = 0

    def get_level(self, actuator):
        if (actuator not in self.actuators):
            raise Exception('Actuator does not exist')
        return self.levels[actuator]

    def set_level(self, actuator, level):
        if (actuator not in self.actuators):
            raise Exception('Actuator does not exist')
        try:
            if (level < 0 or level > 100):
                raise Exception('Wrong level entry (between 0 and 100)')
        except TypeError:
            raise Exception('Wrong type, integer (between 0 and 100) expected')

        self.levels[actuator] = level

    def get_orientation(self):
        return self.orientation

    def set_orientation(self, orientation):
        try:
            if (orientation < 0 or orientation > 360):
                raise Exception('Wrong orientation')
        except TypeError:
            raise Exception('Wrong type, integer (between 0 and 360) expected')
        self.orientation = orientation

    def get_position(self):
        return self.position

    def set_position(self, point):
        self.position = point

    def is_pressed(self):
        return self.isPressed

    def set_pressed(self, value):
        self.isPressed = value
