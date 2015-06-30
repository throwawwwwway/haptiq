import app.conf as cf      # noqa

from enum import Enum


def gen_oscillation(height, steps):
    "height is from bottom to top and steps can be seen as a frequency"
    return [i - height / 2 for i in range(0, height + 1, steps)]


class Context(Enum):
    on, hot, cold, outrange = 1, 2, 3, 4

    @staticmethod
    def which(distance):
        return Context.on if distance < 10 else\
            Context.hot if distance < 50 else\
            Context.cold if distance < 100 else\
            Context.outrange


class Behavior(object):

    default = 10
    max_iter = 255
    _iter = 0

    node_level = {1: 30, 2: None, 3: None, 4: 0}
    link_level = {1: 30, 2: 30, 3: 0, 4: 0}

    def __init__(self):
        self.sequence = [Behavior.default]
        self.context = Context.outrange
        self.actuators = None

    def apply(self):
        if self.actuators is None:
            return
        for act in self.actuators:
            act.level += self.sequence[Behavior._iter % len(self.sequence)]


class NodeBehavior(Behavior):
    def __init__(self):
        super().__init__()

    def update(self, coord, actuators):
        context = Context.which(coord['distance'])
        if (actuators == self.actuators and context == self.context):
            return  # nothing has changed from last time

        self.context = context
        self.actuators = actuators
        if context == Context.hot:
            self.sequence = gen_oscillation(20, 5)
        elif context == Context.cold:
            self.sequence = gen_oscillation(20, 2)
        else:  # on, outrange
            self.sequence = [Behavior.node_level[context.value]]


class LinkBehavior(Behavior):
    def __init__(self):
        super().__init__()

    def update(self, coord, actuators):
        self.context = Context.which(coord['distance']) if coord is not None else Context.outrange
        self.actuators = actuators
        self.sequence = [Behavior.link_level[self.context.value]]
