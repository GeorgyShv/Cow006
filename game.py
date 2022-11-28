from __future__ import annotations

"""
Игра Корова 006
"""

class Game:
    def __init__(self):
        pass

    @staticmethod
    def create(player_names):
        pass

    @staticmethod
    def load(game_data: dict) -> Game:
        return Game()

    def save(self) -> dict:
        return {}

    def run(self):
        for round in range(self.hand_size()):
            close_cards = {}              # {Card(25): self.player[0], Card(2): self.player[1]}
            # все игроки кладут карты (закрытые)
            for player in self.players:
                card = player.choose_card()
                close_cards[card] = player
            # когда все игроки положили карты, они переворачиваются и кладутся по правилам
            for card in sorted(close_cards):
                player = close_cards[card]
                irow = self.table.playable(card)   # номер ряда или -1, если карта слишком маленькая
                if irow == -1:
                    # карта слишком маленькая
                    irow = player.choose_row(self.table)
                    self.table[irow].add(card)
                    player.add_score(self.table.fire_row(irow))
                else:
                    self.table[irow].add(card)     # [] Table.__getitem__
                    if len(self.table) == 6:        # 6 Table.MAX_ROW_LEN
                        # сжигаем ряд
                        player.add_score(self.table.fire_row(irow))








    def winner_congrats(self):
        pass

    def hand_size(self):
        """Возвращает сколько карт у игроков"""
        pass


import data
game = Game.load(data.game_data)
game.run()
game.winner_congrats()