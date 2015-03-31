class MPattern(object):

    def __init__(self, patterns=[]):
        self.patterns = patterns

    def next_levels(self):
        return [pattern.next_level() for pattern in self.patterns]


class Pattern(object):

    def __init__(self, sequence=[]):
        self.sequence = sequence
        self.cursor = 0

    def next_level(self):
        level = self.sequence[self.cursor]
        self.cursor = (self.cursor + 1) % len(self.sequence)
        return level


class Oscilate(Pattern):  # TODO

    def __init__(self, min_level=0, top_level=100, steps=50):

        seq = list(range(min_level, top_level + 1, steps))
        r_seq = list(seq)
        r_seq.reverse()
        r_seq.pop(0)
        r_seq.pop(-1)
        # step = (top_level - min_level + 1) / (steps / 2.) # float
        # ll = [top_level]
        # for (x in range(50)):
        #     level = int(100-x*step)
        #     ll = [level] + ll + [level]
        # levels = range(min_level, top_level)
        # full_seq += half_seq

        super().__init__(seq + r_seq)
