from __future__ import annotations

from card_list import CardList
from card import Card
import random

class Deck (CardList):
  def shuffle (self):
    random.shuffle(self.cards)
  @staticmethod
  def load(cards_int: list(int)) -> Deck:
      return Deck(CardList.load(cards_int))

class Hand(CardList):
  def remove (self, card:Card):
    self.cards.remove(card)

  @staticmethod
  def load(cards_int: list(int)) -> Hand:
      return Hand(CardList.load(cards_int))