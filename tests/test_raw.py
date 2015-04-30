import pytest

from app.raw import Raw, Actuator


@pytest.fixture()
def init_raw():
    east = Actuator(0, 'East')
    north = Actuator(90, 'North')
    west = Actuator(180, 'West')
    south = Actuator(270, 'South')
    return Raw([east, north, west, south])


def test_levels():
    raw = init_raw()
    assert len(raw.actuators) == 4
