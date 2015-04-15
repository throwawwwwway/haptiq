import pytest

from app.raw import Raw, Actuator, Point


@pytest.fixture()
def init_raw():
    actuators = ['actA', 'actB', 'actC', 'actD', 'actE']
    return Raw(actuators)


def test_levels():
    raw = init_raw()
    with pytest.raises(Exception) as excinfo:
        raw.get_level('actZ')
    assert 'Actuator does not exist' in str(excinfo.value)
    with pytest.raises(Exception) as excinfo:
        raw.set_level('actZ', 100)
    assert 'Actuator does not exist' in str(excinfo.value)
    with pytest.raises(Exception) as excinfo:
        raw.set_level('actA', -1)
    assert 'level should be' in str(excinfo.value)
    with pytest.raises(Exception) as excinfo:
        raw.set_level('actA', 101)
    assert 'level should be' in str(excinfo.value)
    with pytest.raises(Exception) as excinfo:
        raw.set_level('actA', 'a')
    assert 'level should be' in str(excinfo.value)
    raw.set_level('actA', 100)
    assert raw.get_level('actA') == 100


def test_get_state():
    raw = init_raw()

    # default
    cur_state = raw.get_state()
    assert cur_state['position'] == Point(0, 0)
    assert cur_state['angle'] == 90

    # changed
    raw.position = Point(10, 100)
    raw.angle = 180
    cur_state = raw.get_state()
    assert cur_state['position'] == Point(10, 100)
    assert cur_state['angle'] == 180


def test_get_actuators_interval():
    east = Actuator(0, 'east')
    north = Actuator(90, 'north')
    west = Actuator(180, 'west')
    south = Actuator(270, 'south')
    actuators = [east, north, west, south]
    raw = Raw(actuators)
    raw.set_all_at(50)

    res = raw.get_actuators_interval(0)
    assert res == [east]
    res = raw.get_actuators_interval(45)
    assert res == [east, north]
    res = raw.get_actuators_interval(90)
    assert res == [north]
    res = raw.get_actuators_interval(135)
    assert res == [north, west]
    res = raw.get_actuators_interval(180)
    assert res == [west]
    res = raw.get_actuators_interval(215)
    assert res == [west, south]
    res = raw.get_actuators_interval(270)
    assert res == [south]
    res = raw.get_actuators_interval(305)
    assert res == [south, east]
    res = raw.get_actuators_interval(360)
    assert res == [east]


def test_get_levels_for_coding():
    east = Actuator(0, 'east')
    north = Actuator(90, 'north')
    west = Actuator(180, 'west')
    south = Actuator(270, 'south')
    actuators = [east, north, west, south]
    raw = Raw(actuators)
    raw.set_all_at(50)

    outrange = Raw.OUTRANGE_NODE
    limit_lvl = Raw.CODED_LEVEL_LIMIT

    # Angle for one actuator
    assert raw.get_levels_for_coding(0, outrange) == {west: limit_lvl}
    assert raw.get_levels_for_coding(90, outrange) == {south: limit_lvl}
    assert raw.get_levels_for_coding(180, outrange) == {east: limit_lvl}
    assert raw.get_levels_for_coding(270, outrange) == {north: limit_lvl}

    # Angle for one actuator, different distances
    coded_level_max = raw.get_levels_for_coding(0, outrange)
    coded_level_medium = raw.get_levels_for_coding(0, 10)
    assert coded_level_max[west] > coded_level_medium[west]
    coded_level_medium_plus = raw.get_levels_for_coding(0, 11)
    assert coded_level_medium_plus[west] > coded_level_medium[west]

    # Angle for two actuators, same ratio
    coded_level = raw.get_levels_for_coding(45, 10)
    assert coded_level[west] == coded_level[south]
    coded_level = raw.get_levels_for_coding(135, 10)
    assert coded_level[east] == coded_level[south]
    coded_level = raw.get_levels_for_coding(225, 10)
    assert coded_level[east] == coded_level[north]
    coded_level = raw.get_levels_for_coding(315, 10)
    assert coded_level[west] == coded_level[north]

    # Angle for two actuators, different ratios
    coded_level = raw.get_levels_for_coding(70, 10)
    assert coded_level[west] < coded_level[south]
    coded_level = raw.get_levels_for_coding(160, 10)
    assert coded_level[east] > coded_level[south]
    coded_level = raw.get_levels_for_coding(250, 10)
    assert coded_level[east] < coded_level[north]
    coded_level = raw.get_levels_for_coding(340, 10)
    assert coded_level[west] > coded_level[north]

    coded_level = raw.get_levels_for_coding(10, 10)
    assert coded_level[west] > coded_level[south]
    coded_level = raw.get_levels_for_coding(100, 10)
    assert coded_level[east] < coded_level[south]
    coded_level = raw.get_levels_for_coding(190, 10)
    assert coded_level[east] > coded_level[north]
    coded_level = raw.get_levels_for_coding(280, 10)
    assert coded_level[west] < coded_level[north]
