from sheep.coordinates import ORIGIN
from sheep.pastures import Pasture


def test_pasture():
    pasture = Pasture(location=ORIGIN)
    assert pasture
