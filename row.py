from __future__ import annotations
from card import Card
from card_list import CardList


class Row(CardList):
    MAX_LEN = 6

    def __repr__(self):
        return super().__repr__()

    def __gt__(self, other) -> bool:
        """ Сравниваем на > два ряда."""
        return self.top() > other.top()

    def top(self) -> Card:
        """ Последняя карта ряда """
        return super().__getitem__(-1)
        # return self.cards[-1]

    def overflow(self) -> bool:
        """ проверяет, есть 6 коров в ряду (True) или еще нет (False)"""
        return super().__len__() == Row.MAX_LEN

    def acceptable(self, card) -> bool:
        """ эту карту card можно положить в конец этого ряда? """
        return self.top() < card

    def cut(self) -> int:
        """ Убирает из ряда все карты. Возвращает количество очков на убранных картах"""
        sc = 0
        cards = self.draw(self.__len__())

        for card in cards:
            sc += card.score
        return sc

    @staticmethod
    def load(cards_int: list(int)) -> Row:
        return Row(CardList.load(cards_int))