from app.network import Point
import app.conf as cf
import itertools


def init_base():
    """ Corresponds to the CD+cup prototype """
    return {
        'top': Point(0.70447188, 0.39590805),
        'bottom': Point(0.70798462, 0.81577765),
        'right': Point(0.82564610, 0.79777598)
    }


def almost_equal(i, j, precision=0.1):
    return (i >= j / (1 + precision) and
            i <= j * (1 + precision))


class PointsHandler(object):

    def __init__(self, raw, points, width=500, height=500):
        self.raw = raw
        self.width = width
        self.height = height
        self.points = points
        self.base = init_base()
        self.dist_tr = self.base['top']._distance_to(self.base['right'])
        self.dist_tb = self.base['top']._distance_to(self.base['bottom'])
        self.dist_rb = self.base['right']._distance_to(self.base['bottom'])

    def manage(self, id, x, y):
        cf.logger.debug("asking to handle: {} for {}".format(
            str(id), str(Point(x, y))))
        point = Point(x * self.width, y * self.height)

        if self.points == 1:
            self.raw.position = point
            return

        if (self.cur_base.get(id) is None and len(self.cur_base) == 3):
            self.cur_base = {}
        self.cur_base[id] = point

        if len(self.cur_base) == 3:
            points = list(self.cur_base.values())
            tbr = self.eval_tbr(points)
            self.raw.position = Point(
                tbr['top']._distance_to(tbr['bottom']),
                tbr['bottom']._distance_to(tbr['right'])
            )
            self.raw.orientation = tbr['bottom']._angle_with(tbr['right'])

    def eval_tbr(self, points):
        """ Evaluates the top, bottom and right points from the given ones """
        if len(points) != 3:
            cf.logger.debug("[eval_tbr] Not 3 points given")
            return {}

        iter = itertools.permutations(range(3), 3)
        for top, bottom, right in iter:
            d_tb = points[top]._distance_to(points[bottom])
            d_tr = points[top]._distance_to(points[right])
            if (almost_equal(d_tb, self.dist_tb) and
                    almost_equal(d_tr, self.dist_tr)):
                return {
                    'top': points[top],
                    'bottom': points[bottom],
                    'right': points[right]
                }
        return None


if __name__ == '__main__':
    pass
