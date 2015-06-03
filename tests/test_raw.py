import pytest

from app.raw import Raw, Actuator, Button
from app.network import Point


@pytest.fixture()
def init_raw_4():
    east = Actuator(0, 'East')
    north = Actuator(90, 'North')
    west = Actuator(180, 'West')
    south = Actuator(270, 'South')
    return Raw([east, north, west, south])


@pytest.fixture()
def init_raw_8():
    east = Actuator(0, 'East')
    north_east = Actuator(45, 'North-East')
    north = Actuator(90, 'North')
    north_west = Actuator(135, 'North-West')
    west = Actuator(180, 'West')
    south_west = Actuator(225, 'South-West')
    south = Actuator(270, 'South')
    south_east = Actuator(315, 'South-East')
    return Raw([
        east, north_east, north, north_west,
        west, south_west, south, south_east])


def test_init_raw():
    raw = init_raw_4()
    assert len(raw.actuators) == 4
    assert raw.orientation == 0
    assert raw.position == Point(0, 0)
    raw = init_raw_8()
    assert len(raw.actuators) == 8
    assert raw.orientation == 0
    assert raw.position == Point(0, 0)


def test_setters():
    raw = init_raw_8()
    raw.orientation = 30
    raw.position = Point(10, 50)
    assert raw.orientation == 30
    assert raw.position == Point(10, 50)


def test_actuator_for_angle():
    east = Actuator(0, 'East')
    north_east = Actuator(45, 'North-East')
    north = Actuator(90, 'North')
    north_west = Actuator(135, 'North-West')
    west = Actuator(180, 'West')
    south_west = Actuator(225, 'South-West')
    south = Actuator(270, 'South')
    south_east = Actuator(315, 'South-East')
    raw = Raw([
        east, north_east, north, north_west,
        west, south_west, south, south_east])
    data = [
        (0, west), (45, south_west), (90, south),
        (135, south_east), (180, east), (225, north_east),
        (270, north), (315, north_west)
    ]
    for angle, act in data:
        assert raw.actuator_for_angle(angle) == act
        assert raw.actuator_for_angle(angle + 10) == act
        assert raw.actuator_for_angle(angle - 10) == act
        assert raw.actuator_for_angle(angle + 10) == act
        assert raw.actuator_for_angle(angle + 25) != act
        assert raw.actuator_for_angle(angle - 25) != act
    raw.orientation = 180
    data = [(i + 180, v) for i, v in data]
    for angle, act in data:
        assert str(raw.actuator_for_angle(angle)) == str(act)
        assert raw.actuator_for_angle(angle + 10) == act
        assert raw.actuator_for_angle(angle - 10) == act
        assert raw.actuator_for_angle(angle + 10) == act
        assert raw.actuator_for_angle(angle + 25) != act
        assert raw.actuator_for_angle(angle - 25) != act


def test_set_all_at():
    raw = init_raw_8()
    for act in raw.actuators:
        assert act.level == 0
    raw.set_all_at(25)
    for act in raw.actuators:
        assert act.level == 25
    raw.set_all_at(100)
    for act in raw.actuators:
        assert act.level == 100


def test_actuators():
    east = Actuator(0, 'East')
    assert 'East' in str(east)
    assert '0' in str(east)
    west = Actuator(90, 'West')
    assert (east > west) is False
    assert (west > east) is False
    west.level = 100
    assert east < west
    assert west > east

    with pytest.raises(Exception):
        east.level = 'a'

    east.level = 110
    assert east.level == 0

    assert east.should_update()
    assert not east.should_update()


def test_buttons():
    central = Button()
    assert central.level == 50
