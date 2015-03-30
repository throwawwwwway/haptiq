import pytest


from app.raw import Raw
from app.raw import Point


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
    assert 'Wrong level entry' in str(excinfo.value)
    with pytest.raises(Exception) as excinfo:
        raw.set_level('actA', 101)
    assert 'Wrong level entry' in str(excinfo.value)
    with pytest.raises(Exception) as excinfo:
        raw.set_level('actA', 'a')
    assert 'Wrong type' in str(excinfo.value)
    raw.set_level('actA', 100)
    assert raw.get_level('actA') == 100


def test_orientation():
    raw = init_raw()
    with pytest.raises(Exception) as excinfo:
        raw.set_orientation(-1)
    assert 'Wrong orientation' in str(excinfo.value)
    with pytest.raises(Exception) as excinfo:
        raw.set_orientation(361)
    assert 'Wrong orientation' in str(excinfo.value)
    with pytest.raises(Exception) as excinfo:
        raw.set_orientation('a')
    assert 'Wrong type' in str(excinfo.value)
    raw.set_orientation(120)
    assert raw.get_orientation() == 120


def test_position():
    raw = init_raw()
    point = Point(1, 0)
    raw.set_position(point)
    assert raw.get_position() == point


def test_pressed():
    raw = init_raw()
    pressed_state = True
    raw.set_pressed(pressed_state)
    assert raw.is_pressed() == pressed_state
    pressed_state = False
    raw.set_pressed(pressed_state)
    assert raw.is_pressed() == pressed_state
