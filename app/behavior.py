import app.conf as cf      # noqa

from enum import Enum


def gen_oscillation(height, steps):
    "height is from bottom to top and steps can be seen as a frequency"
    return [i - height / 2 for i in range(0, height + 1, steps)]


class Context(Enum):
    on = 1
    hot = 2
    cold = 3
    outrange = 4


class Behavior(object):

    default = 5
    max_iter = 255
    _iter = 0

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
    on = 30

    def __init__(self):
        super().__init__()

    def update_if_necessary(self, context, actuators, coord):
        if (actuators == self.actuators and context == self.context):
            return  # nothing has changed from last time

        self.context = context
        self.actuators = actuators
        if context == Context.on:
            self.sequence = [NodeBehavior.on]
        elif context == Context.hot:
            self.sequence = gen_oscillation(10, 5)
        elif context == Context.cold:
            self.sequence = gen_oscillation(10, 2)
        elif context == Context.outrange:
            self.sequence = [0]


class LinkBehavior(Behavior):
    on = 30

    def __init__(self):
        super().__init__()

    def update(self, context, actuators, coord):
        # We should update the behavior
        self.context = context
        self.actuators = actuators
        lvl = 30
        if context == Context.on:
            self.sequence = [LinkBehavior.on]
        elif context == Context.hot:
            self.sequence = [lvl]
        else:
            self.sequence = [0]
