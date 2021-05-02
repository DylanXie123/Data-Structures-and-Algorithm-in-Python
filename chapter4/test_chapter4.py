from chapter4.move_tower import moveTower
from chapter4.to_str import to_str


def test_to_str():
    s = to_str(102, 2)
    assert s == '1100110'

def test_move_tower():
    moveTower(4, 'A', 'B', 'C')