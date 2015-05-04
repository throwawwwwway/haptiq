from app.network import Point
import app.conf as cf
import itertools


def init_base():
    return {
        'top': Point(0, 0),
        'bottom': Point(0, 20),
        'right': Point(10, 20)
    }


class PointsHandler(object):

    def __init__(self, raw=None, width=500, height=500):
        self.raw = raw
        self.width = width
        self.height = height
        self.base = init_base()
        self.dist_tr = self.base['top']._distance_to(self.base['right'])
        self.dist_tb = self.base['top']._distance_to(self.base['bottom'])
        self.dist_rb = self.base['right']._distance_to(self.base['bottom'])

    def manage(self, id, x, y):
        cf.logger.debug("asking to handle: {} for {}".format(
            str(id), str(Point(x, y))))
        point = Point(x * self.width, y * self.height)
        # if self.magic_l.get(id) is None:
        #     if len(self.magic_l) >= 3:
        #         self.magic_l = {}
        #     self.magic_l[id] = point
        # if len(self.magic_l) < 3:
        #     return

        self.raw.position = point

    def retrieve_tbr(self, points):
        if len(points) != 3:
            cf.logger.debug("[retrieve_tbr] Not 3 points given")
            return {}

        iter = itertools.permutations(range(3), 3)
        for top, bottom, right in iter:
            if (points[top]._distance_to(points[bottom]) == self.dist_tb and
                    points[top]._distance_to(points[right]) == self.dist_tr):
                return {
                    'top': points[top],
                    'bottom': points[bottom],
                    'right': points[right]
                }
        return None

    def compute_angle(self, points):
        tbr = self.retrieve_tbr(points)
        return tbr['bottom']._angle_with(tbr['right'])


if __name__ == '__main__':
    pts_handler = PointsHandler()
    res = pts_handler.compute_angle(
        [Point(0, 0), Point(-20, 0), Point(-20, 10)])
    print(str(res))
