"""
A move occurs when a player claims a pasture.
"""
from sheep.pastures import Pasture


class Move:
    def __init__(self, *, player: int, pasture: Pasture) -> None:
        self.player = player
        self.pasture = pasture

    def __repr__(self) -> str:
        return f'Player {self.pasture}: {self.pasture}'
