from __future__ import annotations

from abc import ABC, abstractmethod

from hand_and_deck import Hand, Deck
from card import Card
from table import Table


class Player(ABC):
    def __init__(self, name: str):
        self.name = name
        self.hand = Hand([])
        self.score = 0

    @staticmethod
    def create(name: str, deck: Deck, interactive=False) -> Player:
        if interactive:
            player = PlayerHuman(name)
        else:
            player = PlayerAI(name)
        player.hand.add_full_hand(deck)
        return player

    @staticmethod
    def load(data: dict) -> Player:
        """
        Получает данные, возвращает игрока
        {
            'name': 'Bob',
            'hand': [25, 67],
            'score': 4,
            'interactive': True
        },
        """
        if data['interactive']:
            player = PlayerHuman(data['name'])
        else:
            player = PlayerAI(data['name'])
        player.hand = Hand.load(data['hand'])
        player.score = data['score']
        return player

    def __repr__(self):
        return f'{self.name} ({self.score}) {self.hand}'

    @abstractmethod
    def choose_card(self) -> Card:
        pass

    def add_score(self, score: int):
        self.score += score

    @abstractmethod
    def choose_row(self, table: Table) -> int:
        pass


class PlayerAI(Player):
    def choose_card(self) -> Card:
        # первую попавшуюся карту
        card = self.hand.draw()[0]
        return card

    def choose_row(self, table: Table) -> int:
        rowi = 0
        return rowi


class PlayerHuman(Player):
    def choose_row(self, table: Table) -> int:
        while True:
            rowi = int(input('Введите номер ряда: '))
            print(f'len = {len(table)}')
            if rowi < 0 or rowi >= len(table):
                print('Такого ряда нет')
            else:
                return rowi

        return rowi  #

    def choose_card(self) -> Card:
        while True:
            print(self)
            i = int(input('Введите карту, которую хотите выбрать: '))
            card = Card(i)
            try:
                self.hand.remove(card)
            except ValueError:
                print('Такой карты у вас нет')
            else:
                break
        return card