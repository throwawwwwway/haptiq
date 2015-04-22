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

    default = 20
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
    on = 20

    def __init__(self):
        super().__init__()

    def update_if_necessary(self, context, actuators, coord):
        if (actuators == self.actuators and context == self.context):
            return
        # We should update the behavior
        self.context = context
        self.actuators = actuators
        if context == Context.on:
            self.sequence = [NodeBehavior.on]
        elif context == Context.hot:
            self.sequence = gen_oscillation(20, 20)
        elif context == Context.lukewarm:
            self.sequence = gen_oscillation(20, 10)
        elif context == Context.cold:
            self.sequence = gen_oscillation(20, 5)
        elif context == Context.outrange:
            self.sequence = [0]
        cf.logger.debug("[node] Context is {}, sequence is {}".format(
            context, str(self.sequence)))


class LinkBehavior(Behavior):
    on = 30

    def __init__(self):
        super().__init__()

    def update_if_necessary(self, context, actuators, coord):
        # We should update the behavior
        self.context = context
        self.actuators = actuators
        lvl = 20 - coord['distance'] / 5
        if context == Context.on:
            self.sequence = [LinkBehavior.on]
        elif context == Context.hot or context == Context.lukewarm:
            self.sequence = [lvl]
        elif context == Context.outrange:
            self.sequence = [0]
        cf.logger.debug("[link] Context is {}, sequence is {}".format(
            context, str(self.sequence)))
