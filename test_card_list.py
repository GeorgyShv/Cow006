from card_list import CardList
from card import Card

example_card_list = [Card(4), Card(25), Card(40), Card(59)]

def test_card_list():
    cl = CardList(example_card_list.copy())
    assert repr(cl) == '4 25 40 59'
    assert len(cl) == 4

    cl.add(Card(68))
    assert repr(cl) == '4 25 40 59 68'
    assert len(cl) == 5

    cl.add(Card(101))
    assert repr(cl) == '4 25 40 59 68 101'
    assert len(cl) == 6

    # Работа с пустым списком
    cl = CardList([])
    assert repr(cl) == ''
    assert len(cl) == 0

    cl.add(Card(2))
    assert repr(cl) == '2'
    assert len(cl) == 1

    #cl = CardList([])
    #cl.draw(10)
    #assert len(cl) = 10

def test_card_list_i():
    cl = CardList(example_card_list.copy())
    assert repr(cl) == '4 25 40 59'
    # cl.__getitem__(0)
    assert cl[0] == Card(4)
    assert cl[-1] == Card(59)
    assert cl[2] == Card(40)

def test_card_list_draw():
    cl = CardList(example_card_list.copy())
    assert repr(cl) == '4 25 40 59'

    # draw card 4
    card = cl.draw()
    print(cl)
    print(card)
    assert repr(cl) == '25 40 59'
    assert card == [Card(4)]
    assert repr(card) == '[4(1)]'

    # draw card 25
    card = cl.draw()
    assert repr(cl) == '40 59'
    assert card == [Card(25)]


    # draw 3 cards
    cl = CardList(example_card_list.copy())
    cards = cl.draw(3)
    assert repr(cl) == '59'
    assert cards == [Card(4), Card(25), Card(40)]