from player import Player, PlayerAI, PlayerHuman
from card import Card
from table import Table


def test_abc():
    p = PlayerAI('AI-1')
    print(p)


def test_human():
    p = {
        'name': 'Bob',
        'hand': [25, 67],
        'score': 4,
        'interactive': True
    }
    player = Player.load(p)
    assert repr(player) == 'Bob (4) 25 67'


def test_choose_card():
    p = {
        'name': 'Bob',
        'hand': [25, 67, 33, 100, 87],
        'score': 4,
        'interactive': True
    }
    player = Player.load(p)
    assert repr(player) == 'Bob (4) 25 67 33 100 87'
    # assert repr(player) == 'Bob (4) 312'

    print('Введите число 67')
    assert player.choose_card() == Card(67)
    assert repr(player) == 'Bob (4) 25 33 100 87'
    print('Введите число 25')
    assert player.choose_card() == Card(25)
    assert repr(player) == 'Bob (4) 33 100 87'

    print('Введите число 103, потом число 33')
    assert player.choose_card() == Card(33)
    assert repr(player) == 'Bob (4) 100 87'


def test_choose_row():
    p = {
        'name': 'Bob',
        'hand': [25, 67, 33, 100, 87],
        'score': 4,
        'interactive': True
    }
    player = Player.load(p)
    table_data = [
        [2],
        [25, 30]
    ]
    table = Table.load(table_data)
    print(table)
    print('Введите число 1')
    assert player.choose_row(table) == 1
    print(table)

    print('Введите число 2, потом введите число 0')
    assert player.choose_row(table) == 0