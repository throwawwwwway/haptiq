from app.network import Point
import app.conf as cf


def get_triangle(points):

        ab = points[0]._distance_to(points[1])
        ac = points[0]._distance_to(points[2])
        bc = points[1]._distance_to(points[2])

        if ab < ac and ab < bc:
            top, left, right = 2, 0, 1
        elif ac < ab and ac < bc:
            top, left, right = 1, 0, 2
        elif bc < ac and bc < ab:
            top, left, right = 0, 1, 2
        else:
            return None

        return {
            'top': points[top],
            'left': points[left],
            'right': points[right]
        }


class Handler(object):

    def __init__(self, raw, width=500, height=500):
        self.raw = raw
        self.width = width
        self.height = height
        self.points = {}
        self.waiting_update = False

    def update_position(self):
        n_pts = len(self.points)
        if n_pts < 1:
            return
        x, y = 0, 0
        for pt in self.points.values():
            x += pt.x
            y += pt.y
        self.raw.position = Point(
            int(x / n_pts * self.width),
            int(y / n_pts * self.height)
        )

    def update_orientation(self):
        triangle = get_triangle(list(self.points.values()))
        if triangle is None:
            cf.logger.debug("Triangle not found")
        else:
            middle = Point(
                (triangle['right'].x + triangle['left'].x) / 2,
                (triangle['right'].y + triangle['left'].y) / 2,
            )
            self.raw.orientation = middle._angle_with(triangle['top'])

    def manage(self, points):
        if not self.waiting_update:
            self.waiting_update = True
            self.points = {id: Point() for id in points}

    def update_raw(self):
        if self.waiting_update:
            self.update_position()
            if len(self.points) == 3:
                self.update_orientation()
            self.waiting_update = False

# def manage(self, id, x, y):
#     # cf.logger.debug("Point {}: ({}, {}) handled".format(
#     #     str(id), str(x), str(y)))
#     if len(self.points) == 3 and id not in self.points:
#         cf.logger.debug("New point")
#         self.points = {id: Point(x, y)}
#     else:
#         self.points[id] = Point(x, y)
#         self.set_position()
#         if len(self.points) < 3:
#             cf.logger.debug("Not enough points")
#             return
#         triangle = get_triangle(list(self.points.values()))
#         if triangle is None:
#             print("Triangle not found")
#             for id, pt in self.points.items():
#                 print("{}: {}".format(id, str(pt)))
#         else:
#             middle = Point(
#                 (triangle['right'].x + triangle['left'].x) / 2,
#                 (triangle['right'].y + triangle['left'].y) / 2,
#             )
#             self.raw.orientation = middle._angle_with(triangle['top'])


if __name__ == '__main__':
    pass
