from typing import List

from sheep.moves import Move


class Board:
    def __init__(self) -> None:
        self.moves: List[Move] = []
