class Table:
    def __init__(self):
        pass

    @staticmethod
    def create(deck: Deck) -> Table:
        pass

    @staticmethod
    def load(table_data: dict) -> Table:
        pass

    def __repr__(self):
        pass

    def __len__(self):
        pass

    def __getitem__(self, i: int):
        pass

    def find_row(self, card: Card) -> int | None:
        """ ищет, в какой ряд нужно положить эту карту,
        возвращает индекс ряда или None,
        если карту нельзя положить ни в один ряд """
        # Ищем наименьшую разницу между последней картой каждого ряда
        pass

    @staticmethod
    def load(table):
        pass