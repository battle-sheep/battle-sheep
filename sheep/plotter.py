"""
Visualize the board using matplotlib.

This module munges cubic coordinates to cartesian coordinates for matplotlib.
It is a stopgap solution until a proper UI is built.

Usage:
    $ python -m sheep.plotter
"""
from typing import List

import matplotlib.pyplot as plt

from sheep.coordinates import CUBIC_DIRECTIONS, ORIGIN, CubicPoint
from sheep.moves import Move
from sheep.pastures import Pasture

MATBPLOTLIB_BLACK = 'k'


class CartesianPoint:
    def __init__(self, *, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

    @classmethod
    def from_cubic(cls, cubic: CubicPoint) -> 'CartesianPoint':
        x = cubic.x / 2 - cubic.y / 2
        y = cubic.x / 6 + cubic.y / 6 - cubic.z / 3
        return CartesianPoint(x=x, y=y)


def plot(moves: List[Move]) -> None:
    """
    Plot the moves on a hexagonal grid using matplotlib.
    """
    print('Plotting moves:')
    for move in moves:
        print(f'  {move}')
    figure, ax = plt.subplots(ncols=1, sharey=True, figsize=(5, 5))

    cubic_points = [move.pasture.location for move in moves]
    print()
    print('Cubic points:')
    for cubic_point in cubic_points:
        print(f'  {cubic_point}')

    cartesian_points = [
        CartesianPoint.from_cubic(cubic_point)
        for cubic_point in cubic_points
    ]
    print()
    print('Cartesian points:')
    for cartesian_point in cartesian_points:
        print(f'  {cartesian_point}')

    x = list(map(lambda point: point.x, cartesian_points))
    y = list(map(lambda point: point.y, cartesian_points))
    counts = list(map(lambda move: move.player, moves))

    xsize = max(x) - min(x)
    xsize = max(1, xsize)
    ysize = max(y) - min(y)
    ysize = max(1, ysize)
    gridsize = (int(xsize), int(ysize))
    print(f'gridsize: {gridsize}')
    hexbin = ax.hexbin(
        x, y,
        C=counts,
        gridsize=gridsize,
        edgecolors=MATBPLOTLIB_BLACK,
    )

    xmin = min(x) - 0.5
    ymin = min(y) - 0.5
    xmax = max(x) + 0.5
    ymax = max(y) + 0.5
    ax.axis([xmin, xmax, ymin, ymax])

    figure.colorbar(hexbin, ax=ax)

    plt.show()


if __name__ == '__main__':
    test_moves: List[Move] = []
    for player in range(6):
        direction = CUBIC_DIRECTIONS[player]
        for distance in range(10):
            test_moves.append(Move(
                player=player,
                pasture=Pasture(ORIGIN + direction * distance)
            ))
    plot(test_moves)
