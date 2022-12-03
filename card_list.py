from __future__ import annotations
from card import Card

cl = [Card(5), Card(101), Card(43)]


class CardList:
    def __init__(self, cards: list[Card]):
        self.cards = cards

    def add(self, card: Card):
        """ Add card to list. """
        self.cards.append(card)

    def draw(self, count=1) -> Card:
        """ Return count cards from card list, remove these cards from the list."""
        deleted_cards = self.cards[:count]
        self.cards = self.cards[count:]
        return deleted_cards

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, i: int) -> Card:
        return self.cards[i]

    def __repr__(self) -> str:
        return ' '.join([str(card) for card in self.cards])

    @staticmethod
    def load(cards_int: list(int)) -> list[Card]:
        cards = []
        for num in cards_int:
            cards.append(Card(num))
        # cards = [Card(num) for num in cards_int]
        return cards

# cl.draw(10)