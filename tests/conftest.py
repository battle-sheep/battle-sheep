import pytest

from sheep.boardpieces import BoardPiece
from sheep.coordinates import CUBIC_DIRECTIONS, ORIGIN
from sheep.pastures import Pasture


@pytest.fixture
def pasture():
    return Pasture(ORIGIN)


@pytest.fixture
def boardpiece():
    pastures = [
        Pasture(ORIGIN),
        Pasture(ORIGIN + CUBIC_DIRECTIONS[0]),
        Pasture(ORIGIN + CUBIC_DIRECTIONS[1]),
        Pasture(ORIGIN + CUBIC_DIRECTIONS[2]),
    ]
    boardpiece = BoardPiece(pastures=pastures)
    return boardpiece
