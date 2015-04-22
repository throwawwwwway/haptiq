import conf as cf


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
        cf.logger.debug('Pattern returns {} for next level'.format(level))
        return level


class Oscilate(Pattern):

    def __init__(self):
        # min_level=0, top_level=100, steps=50,
        seq = list(range(0, 100, 9))
        r_seq = list(seq)
        r_seq.reverse()
        r_seq.pop(0)
        r_seq.pop(-1)

        super().__init__(seq + r_seq)
