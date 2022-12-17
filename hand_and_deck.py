from __future__ import annotations

from card_list import CardList
from card import Card
import random


class Deck(CardList):
    def shuffle(self):
        random.shuffle(self.cards)

    @staticmethod
    def load(cards_int: list(int)) -> Deck:
        return Deck(CardList.load(cards_int))


class Hand(CardList):
    MAX_HAND_SIZE = 10

    def remove(self, card: Card):
        self.cards.remove(card)

    def add_full_hand(self, deck: Deck):
        """ Добавляет MAX_HAND_SIZE карт в руку"""
        for i in range(Hand.MAX_HAND_SIZE):
            self.add(deck.draw()[0])

    @staticmethod
    def load(cards_int: list(int)) -> Hand:
        return Hand(CardList.load(cards_int))