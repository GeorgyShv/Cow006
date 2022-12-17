from __future__ import annotations

from table import Table
from player import Player
from hand_and_deck import Hand, Deck
from card import Card

"""
Игра Корова 006
"""


class Game:
    def __init__(self):
        self.players = []
        self.table = None

    def __repr__(self):
        return f'{self.table}\n-----\n' + '\n'.join([repr(p) for p in self.players])

    @staticmethod
    def create(player_names):
        game = Game()
        deck = Deck(Card.all_cards())
        deck.shuffle()
        game.table = Table.create(deck)
        game.players = [Player.create(name, deck, i == 0) for i, name in enumerate(player_names)]
        return game

    @staticmethod
    def load(game_data: dict) -> Game:
        game = Game()
        game.table = Table.load(game_data['table'])
        game.players = [Player.load(player_data) for player_data in game_data['players']]
        return game

    def save(self) -> dict:
        return {}

    def run(self):
        print(self)
        for round in range(self.hand_size()):
            close_cards = {}  # {Card(25): self.player[0], Card(2): self.player[1]}
            # все игроки кладут карты (закрытые)
            for player in self.players:
                card = player.choose_card()
                print(f'Player {player.name} choose card {card}')
                close_cards[card] = player
            # когда все игроки положили карты, они переворачиваются и кладутся по правилам
            for card in sorted(close_cards):
                player = close_cards[card]
                irow = self.table.find_row(card)  # номер ряда или None, если карта слишком маленькая
                print(f'Place card {card} ({player.name}) at row {irow}')
                if irow is None:
                    # карта слишком маленькая
                    irow = player.choose_row(self.table)
                    player.add_score(self.table.fire_row(irow))
                    self.table[irow].add(card)
                    print(f'{player} choose row {irow}')
                else:
                    if len(self.table[irow]) == 6 - 1:  # 6 Table.MAX_ROW_LEN
                        # сжигаем ряд
                        print(f'Fire row {irow}!!!')
                        player.add_score(self.table.fire_row(irow))
                        print(f'Получает карты: {player}')
                    self.table[irow].add(card)  # [] Table.__getitem__

                print(self.table)
                print('-----')

    def winner_congrats(self):
        """ Находит игроков, которые победили (набрали меньше всего очков, их может быть 1 или больше). Выводит надпись Игрок имя победитель, очки."""
        scores = [player.score for player in self.players]  # Список очков игроков
        winner_score = min(scores)  # Количество очков победителя
        print(winner_score)
        for player in self.players:
            if player.score == winner_score:
                print(player.name, 'выиграл!')
                # return f'Поздравляем, {player.name} выиграл!'

    def hand_size(self):
        """Возвращает сколько карт у игроков"""
        return len(self.players[0].hand)


'''
import data
game = Game.load(data.game_data)
game.run()
game.winner_congrats()
'''