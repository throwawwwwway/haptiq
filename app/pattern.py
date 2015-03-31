class Pattern(object):

    def __init__(self, sequence=[]):
        self.sequence = sequence
        self.cursor = 0

    def next_level(self):
        level = self.sequence[self.cursor]
        self.cursor = (self.cursor + 1) % len(self.sequence)
        return level

class MPattern(object):

    def __init__(self, patterns=[]):
        self.patterns = patterns

    def next_levels(self):
        return [pattern.next_level() for pattern in self.patterns]