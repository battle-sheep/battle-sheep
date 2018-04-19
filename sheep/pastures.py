"""
Pastures are locations that may be claimed by a player. A pasture may only be
claimed once.
"""
from typing import Optional

from sheep.coordinates import CubicPoint


class Pasture:
    def __init__(self, location: CubicPoint) -> None:
        self.location = location
        self.player: Optional[int] = None

    def claim(self, player: int) -> None:
        if self.player is None:
            raise Exception(
                'Player {player} cannot claim pasture {self} that is already '
                'claimed by player {self.player}!'
            )
        self.player = player
