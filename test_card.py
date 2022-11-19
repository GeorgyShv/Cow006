from card import Card


def test_create():
    card = Card(25)
    print(card)  # str(card) --> card.__str__
    print(str(card))  # repr(card) --> card.__repr__

    assert str(Card(25)) == '25'
    print(str(card))
    assert str(card) == '25'

    # card_list = [Card(1), Card(34), Card(25)]
    # print(card_list)
    # assert str(card_list) == '[1(0), 34(0), 25(0)]'


def check_one_score(num, expected_score):
    card = Card(num)
    print(repr(card))
    assert repr(card) == f'{num}({expected_score})'


def test_score():
    check_one_score(25, 2)
    check_one_score(30, 3)
    check_one_score(55, 7)
    check_one_score(44, 5)
    check_one_score(76, 1)
    check_one_score(40, 3)
    check_one_score(15, 2)
    check_one_score(81, 1)
    check_one_score(66, 5)