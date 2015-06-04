import pytest

from app.network import which_context, Node, Point


@pytest.fixture()
def fixture():
    return


def test_which_context():
    assert which_context(0) != which_context(50)
    assert which_context(0) != which_context(100)
    assert which_context(100) != which_context(50)


def test_node():
    anode = Node(10, 5)
    assert anode.x == 10 * Node.base_x
    assert anode.y == 5 * Node.base_y
    assert "NODE" in str(anode)


def test_point_distance():
    anode = Point(50, 50)
    bnode = Point(50, 50)
    assert anode == bnode
    bnode.x = 10
    assert anode != bnode
    anode = Point(50.197, 50.197)
    data = [
        Point(60.197, 50.197),
        Point(40.197, 50.197),
        Point(50.197, 60.197),
        Point(50.197, 40.197)
    ]
    for pt in data:
        assert anode._distance_to(pt) == 10, "failed for {}".format(str(pt))
        assert pt._distance_to(anode) == 10
    assert anode._distance_to(Point(50, 50)) != 0


def test_point_angle():
    anode = Point(50, 50)
    data = [
        (Point(60, 50), 0),
        (Point(50, 60), 270),
        (Point(50, 40), 90),
        (Point(40, 50), 180)
    ]
    for pt, angle in data:
        angle_m = anode._angle_with(pt)
        assert abs(angle_m - angle) <= angle*0.01, "failed for {}, {}".format(str(pt), angle)

