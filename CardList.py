class CardList:
    def __init__(self):
        """ Пустой список, карты добавляем через add """
        pass

    def add(self, card: Card):
        pass

    def draw(self) -> Card:
        """ Удаляет карту из списка, возвращает удаленную карту. """
        pass

    def __len__(self):
        pass

    def __getitem__(self, i: int):
        pass

    def __repr__(self):
        pass


class Deck(CardList):
    def __init__(self, cards: list(Card)):
        pass

    def shuffle(self):
        """ Перемешать колоду """
        pass


class Hand(CardList):
    def remove(self, card: Card):
        """ Удаляет из руки карту card """
        pass

    @staticmethod
    def load(cards: list(int)) -> Hand:
        pass