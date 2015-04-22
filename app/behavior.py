import conf as cf
from enum import Enum


def gen_oscillation(height, speed):
    return [i - height / 2 for i in range(0, height + 1) if i % speed == 0]


class Context(Enum):
    on = 1
    hot = 2
    lukewarm = 3
    cold = 4
    outrange = 5


class Behavior(object):

    default = 25
    on = 50
    max_iter = 100
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

    def __init__(self):
        super().__init__()

    def update_if_necessary(self, context, actuators, coord):
        if (actuators == self.actuators and context == self.context):
            return
        # We should update the behavior
        self.context = context
        self.actuators = actuators
        if context == Context.on:
            self.sequence = [Behavior.on]
        elif context == Context.hot:
            self.sequence = gen_oscillation(25, 20)
        elif context == Context.lukewarm:
            self.sequence = gen_oscillation(25, 10)
        elif context == Context.cold:
            self.sequence = gen_oscillation(25, 5)
        elif context == Context.outrange:
            self.sequence = [0]
        cf.logger.debug("New sequence is: {}".format(str(self.sequence)))


class LinkBehavior(Behavior):

    def __init__(self, actuators):
        super().__init__(actuators)

    def update_behavior(self, coord):
        self.sequence = [Behavior.default]
