import app.conf as cf      # noqa

from enum import Enum


def gen_oscillation(height, steps):
    "Height is from bottom to top and steps can be seen as a frequency."
    return [i - height / 2 for i in range(0, height + 1, steps)]


class Context(Enum):
    on, hot, cold, outrange = 1, 2, 3, 4

    @staticmethod
    def which(distance):
        if distance < 10:
            return Context.on
        elif distance < 50:
            return Context.hot
        elif distance < 100:
            return Context.cold
        else:
            return Context.outrange


class Behavior(object):

    default = 10
    max_iter = 255
    _iter = 0

    node_level = {1: 30, 2: None, 3: None, 4: 0}
    link_level = {1: 30, 2: 30, 3: 0, 4: 0}

    def __init__(self):
        self.sequence = [Behavior.default]

    def apply(self, actuators):
        for act in actuators:
            act.level += self.sequence[Behavior._iter % len(self.sequence)]


class NodeBehavior(Behavior):
    def __init__(self):
        super().__init__()

    def update(self, context):
        if context == Context.hot:
            self.sequence = gen_oscillation(20, 5)
        elif context == Context.cold:
            self.sequence = gen_oscillation(20, 2)
        else:  # on, outrange
            self.sequence = [Behavior.node_level[context.value]]


class LinkBehavior(Behavior):
    def __init__(self):
        super().__init__()

    def update(self, context):
        self.sequence = [Behavior.link_level[context.value]]
