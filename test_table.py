import random
from card import Card
from hand_and_deck import Deck
from table import Table
from row import Row

r1 = [Card(3), Card(14), Card(24)]
r2 = [Card(45), Card(54)]
r3 = [Card(6), Card(10), Card(15), Card(20), Card(32)]
r4 = [Card(2)]


def test_table_rows():
    table_data = [
        [42],
        [3],
        [67],
        [25, 30]
    ]
    print(f'table_data = {table_data}')
    table = Table.load(table_data)
    print(f'table={table}')
    print('-----')
    s = '''0: 42
1: 3
2: 67
3: 25 30'''
    assert repr(table) == s


def test_table_create():
    random.seed(10)
    deck = Deck(Card.all_cards())
    deck.shuffle()
    # print(deck.draw())
    # print(deck.draw())
    # print(deck.draw())
    # print(deck.draw())
    table = Table.create(deck)  # 22 81 66 41 ....
    print(table)
    print('-----')

    s = '''0: 22
1: 81
2: 66
3: 41'''
    assert repr(table) == s


def test_table_len():
    table_data = [[42],
                  [3],
                  [67],
                  [25, 30]
                  ]
    table = Table.load(table_data)
    print(repr(table))
    print('-----')
    # проверили длину Row
    assert len(table[0]) == 1
    assert len(table[1]) == 1
    assert len(table[2]) == 1
    assert len(table[3]) == 2
    # проверить len для Table ?
    assert len(table) == 4


def test_table_i():
    # getitem Никита
    table_data = [
        [42],
        [3],
        [67],
        [25, 30]
    ]
    table = Table.load(table_data)
    row1 = Row([Card(42)])
    # row2 = Row([Card(3)])
    row3 = Row([Card(67)])
    row4 = Row([Card(25), Card(30)])

    print(table[0], type(table[0]))
    print(row1, type(row1))

    assert table[0] == row1
    assert table[2] == row3
    assert table[3] == row4


def test_acceptable():
    table_data = [
        [42],
        [3],
        [67],
        [25, 30]
    ]
    # print(f'table_data = {table_data}')
    table = Table.load(table_data)
    print(table)
    print('-----')

    # больше любого ряда
    irow = table.find_row(Card(100))
    assert irow == 2

    # очень маленькая карта
    irow = table.find_row(Card(2))
    assert irow == None

    # один ряд меньше этой карты
    irow = table.find_row(Card(10))
    assert irow == 1

    # два ряда меньше этой карты
    irow = table.find_row(Card(33))
    assert irow == 3


def test_table_fire_row():
    table_data = [
        [42],
        [3],
        [67],
        [25, 30]
    ]
    # print(f'table_data = {table_data}')
    table = Table.load(table_data)
    print(table)
    print('-----')

    expected_text = '''0: 42
1: 3
2: 67
3: 25 30'''

    assert repr(table) == expected_text

    # убираем ряд с картой 3
    score = table.fire_row(1)
    assert score == 1
    expected_text = '''0: 42
1: 
2: 67
3: 25 30'''
    assert repr(table) == expected_text

    # убираем ряд с картами 25 30
    score = table.fire_row(3)
    assert score == 5
    expected_text = '''0: 42
1: 
2: 67
3: '''
    assert repr(table) == expected_text