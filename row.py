class Row(CardList):
    def __repr__(self):
        pass

    def __lt__(self, other) -> bool:
        """ Нужно сравнивать какой ряд больше подходит для карты, т.е. больше остальных."""
        # Берем последнюю карту из каждого ряда и вычисляем наименьшую разницу между ней и картой на руках
        pass

    def top(self) -> Card:
        """ Последняя карта ряда """
        pass

    def overflow(self) -> bool:
        """ проверяет, есть 6 коров в ряду (True) или еще нет (False)"""
        pass

    def acceptable(self, card) -> bool:
        """ эту карту card можно положить в конец этого ряда? """
        pass

    def cut(self) -> int:
        """ Убирает из ряда все карты. Возвращает количество очков на убранных картах"""
        pass

    @staticmethod
    def load(cards: list(int)) -> Hand:
        pass