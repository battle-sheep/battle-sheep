"""
A boardpiece is a connected group of pastures. Boardpieces are only used during
the initial construction of the board.
"""
from typing import List

from sheep.pastures import Pasture


class BoardPiece:
    def __init__(self, pastures: List[Pasture]) -> None:
        self.pastures = pastures
        self.validate()

    def validate(self) -> None:
        if not self.pastures:
            raise Exception('Invalid boardpiece: no pastures!')
        if len(self.pastures) != 4:
            raise Exception('Invalid boardpiece: must contain 4 pastures!')
