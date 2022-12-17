from hand_and_deck import Deck
from hand_and_deck import Hand
from card import Card

example_hand = [Card(2), Card(55), Card(20), Card(54)]
example_deck = [Card(1), Card(25), Card(50), Card(100)]


def test_hand():
    h = Hand(example_hand.copy())
    assert repr(h) == '2 55 20 54'

    h.remove(Card(2))
    assert repr(h) == '55 20 54'
    h.remove(Card(55))
    assert repr(h) == '20 54'
    h.remove(Card(54))
    assert repr(h) == '20'
    h.remove(Card(20))
    assert repr(h) == ''


def test_hand_load():
    hand = Hand.load([5, 1, 63, 18])
    assert repr(hand) == '5 1 63 18'


def test_deck():
    deck = Deck(example_deck.copy())

    for i in range(10):
        deck.shuffle()
        print(deck)
        assert repr(example_deck) != repr(deck)