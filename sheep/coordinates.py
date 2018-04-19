"""
The coordinate system uses "Cube coordinates". See
https://www.redblobgames.com/grids/hexagons/.
"""


class CubicPoint:
    def __init__(self, *, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.validate()

    def validate(self) -> None:
        if self.x + self.y + self.z != 0:
            raise Exception(f'Invalid cubic point: {self}')

    def __repr__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'

    def __add__(self, other) -> 'CubicPoint':
        return CubicPoint(
            x=self.x + other.x,
            y=self.y + other.y,
            z=self.z + other.z,
        )

    def __mul__(self, other: int) -> 'CubicPoint':
        return CubicPoint(
            x=self.x * other,
            y=self.y * other,
            z=self.z * other,
        )


ORIGIN = CubicPoint(x=0, y=0, z=0)
# Directions are pi / 6 apart.
CUBIC_DIRECTION_0 = CubicPoint(x=1, y=-1, z=0)
CUBIC_DIRECTION_1 = CubicPoint(x=1, y=0, z=-1)
CUBIC_DIRECTION_2 = CubicPoint(x=0, y=1, z=-1)
CUBIC_DIRECTION_3 = CubicPoint(x=-1, y=1, z=0)
CUBIC_DIRECTION_4 = CubicPoint(x=-1, y=0, z=1)
CUBIC_DIRECTION_5 = CubicPoint(x=0, y=-1, z=1)
CUBIC_DIRECTIONS = [
    CUBIC_DIRECTION_0,
    CUBIC_DIRECTION_1,
    CUBIC_DIRECTION_2,
    CUBIC_DIRECTION_3,
    CUBIC_DIRECTION_4,
    CUBIC_DIRECTION_5,
]
