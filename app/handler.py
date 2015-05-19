from app.network import Point


class PointsHandler(object):

    def __init__(self, raw, points, width=500, height=500):
        self.raw = raw
        self.width = width
        self.height = height
        self.points = points
        self.magic_l = {}

    def manage(self, id, x, y):
        point = Point(x * self.width, y * self.height)
        if self.points > 1 and self.magic_l.get(id) is None:
            self.magic_l[id] = point
        self.raw.position = point
