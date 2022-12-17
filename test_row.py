from card import Card
from row import Row


def test_top():
    exrow = [Card(2), Card(15), Card(20), Card(54)]
    row = Row(exrow)
    assert row.top() == Card(54)

    row = Row([Card(13)])
    assert row.top() == Card(13)

def test_acceptable():
    exrow = [Card(2), Card(15), Card(20), Card(54)]
    row = Row(exrow)
    assert repr(row) == '2 15 20 54'

    assert row.acceptable(Card(70))
    assert row.acceptable(Card(56))
    assert row.acceptable(Card(102))
    assert not row.acceptable(Card(32))
    assert not row.acceptable(Card(3))

def test_lt():
    row1 = Row([Card(12), Card(15), Card(20), Card(54)])
    row2 = Row([Card(10), Card(64)])
    row3 = Row([Card(33), Card(73)])
    assert row1 < row2
    assert not row2 < row1
    assert row2 < row3
    assert row1 < row3
    assert Row([Card(7)]) < row1