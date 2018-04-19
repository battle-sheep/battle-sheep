import pytest

from sheep.coordinates import CUBIC_DIRECTIONS, ORIGIN, CubicPoint


def test_cubic_0(pasture):
    assert ORIGIN


def test_cubic_directions():
    for cubic_direction in CUBIC_DIRECTIONS:
        assert ORIGIN + cubic_direction


def test_validate():
    with pytest.raises(Exception):
        # Instantiate invalid cubic point.
        CubicPoint(x=1, y=0, z=0)
