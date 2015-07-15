from enum import Enum


class State(Enum):
    on, hot, cold, outrange = 1, 2, 3, 4

    @staticmethod
    def which(distance):
        if distance < 10:
            return State.on
        elif distance < 50:
            return State.hot
        elif distance < 100:
            return State.cold
        else:
            return State.outrange


class Behavior(object):

    default = 10
    max_iter = 255
    _iter = 0

    def __init__(self, seq=None):
        self.sequence = seq if seq is not None else [Behavior.default]

    def next(self):
        return self.sequence[Behavior._iter % len(self.sequence)]

    @staticmethod
    def gen_oscillation(height, steps):
        "Height is from bottom to top and steps can be seen as a frequency."
        return [int(i - height / 2) for i in range(0, height + 1, steps)]
