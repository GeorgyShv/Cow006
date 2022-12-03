from __future__ import annotations
from card import Card
from row import Row
from hand_and_deck import Deck


class Table:

    def __init__(self, rows: list[Row]):
        self.rows = rows

    @staticmethod
    def create(deck: Deck) -> Table:
        ''' Из Deck выбираем n карт '''
        rows = [Row(deck.draw()) for i in range(4)]
        return Table(rows)

    @staticmethod
    def load(table_data: dict) -> Table:
        ''' Загружаем словарь (список списков) с данными и преобразуем в Table '''
        '''
        table_data = [
            [16, 21 ],
            [5, 18, 35, 46, 50],    # этот ряд сгорит при положении 67
            [3],    # в этом ряду меньше всех очков
            [34, 47]
        ]'''
        rows = [Row.load(data) for data in table_data]  # data = table_data[i]
        # a = [7, -3, 2, 1, 4]
        # sq = [x*x for x in a]
        # [49, 9, 4, 1, 16]
        return Table(rows)

    def __repr__(self):
        ''' Вывод стола в текстовом формате '''
        #  '-'.join(map(str, b))
        # s = f'{self.rows[0]}\n{self.rows[1]}\n{self.rows[2]}\n{self.rows[3]}'
        strrows = [f'{i}: {self.rows[i]}' for i in range(4)]
        s = '\n'.join(strrows)
        return s

    def __len__(self):
        return len(self.rows)

    def __getitem__(self, i: int):
        """ Возвращает i-тый ряд"""
        return self.rows[i]

    def find_row(self, card: Card) -> int | None:
        """ ищет, в какой ряд нужно положить эту карту,
        возвращает индекс ряда или None,
        если карту нельзя положить ни в один ряд """
        acc_row = [x for x in self.rows if x.acceptable(card)]
        # карта не подходит ни к одному ряду
        if acc_row == []:
            return None
        # список гарантированно НЕ пустой
        maxrow = max(acc_row)
        for i, row in enumerate(self.rows):
            if row == maxrow:
                return i
        # return None