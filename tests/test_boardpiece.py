import pytest

from sheep.boardpieces import BoardPiece
from sheep.coordinates import ORIGIN
from sheep.pastures import Pasture


def test_boardpiece_valid(boardpiece):
    assert boardpiece


def test_boardpiece_invalid():
    pastures = [
        Pasture(ORIGIN),
    ]
    with pytest.raises(Exception):
        BoardPiece(pastures=pastures)
