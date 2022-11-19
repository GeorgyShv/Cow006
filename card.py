class Card:
    """
    Ранги (очки) коровы:
    2, число кратно 5
    3, число кратно 10
    5, число кратно 11
    7, карта 55
    1 остальные
    """

    def __init__(self, num: int):
        self.num = num
        self.score = Card.__calc_score(num)

    @staticmethod
    def __calc_score(num):
        if num == 55:
            score = 7
        elif num % 11 == 0:
            score = 5
        elif num % 10 == 0:
            score = 3
        elif num % 5 == 0:
            score = 2
        else:
            score = 1
        return score

    def __repr__(self) -> str:
        # print(repr(card)) -> 'call __repr__'
        # print([card1, card2, card3]) -> repr(card1)
        # print(card1)   -> str(card)

        # s = str(self.num) + '(' + str(self.score) + ')'
        # s = self.num + '(' + str(self.score) + ')'
        # s = '{} ({})'.format(self.num, self.score)
        # s = '{self.num} ({self.score})'
        s = f'{self.num}({self.score})'
        return s

    def __str__(self):
        # print(card) -> Card.__str__(card)
        return str(self.num)

    # сравнивает 2 карты по номиналу

# класс закончился