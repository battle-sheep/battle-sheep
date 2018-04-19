from sheep.moves import Move


def test_move(pasture):
    move = Move(player=0, pasture=pasture)
    assert move
