import random

from models.card import Card, CardType, Color


class Deck:

    COLORS = [
        Color.RED,
        Color.BLUE,
        Color.GREEN,
        Color.YELLOW,
    ]

    def __init__(self):
        self.cards = []
        self.create()
        self.shuffle()

    def create(self):
        for color in self.COLORS:
            self.cards.append(
                Card(color, CardType.NUMBER, 0)
            )

            for value in range(1, 10):
                for _ in range(2):
                    self.cards.append(
                        Card(color, CardType.NUMBER, value)
                    )

            for _ in range(2):
                self.cards.append(
                    Card(color, CardType.SKIP)
                )

                self.cards.append(
                    Card(color, CardType.REVERSE)
                )

                self.cards.append(
                    Card(color, CardType.DRAW_TWO)
                )

        for _ in range(4):
            self.cards.append(
                Card(Color.WILD, CardType.WILD)
            )

            self.cards.append(
                Card(Color.WILD, CardType.WILD_DRAW_FOUR)
            )

    def shuffle(self, cards=None):
        """
        Embaralha as cartas fornecidas.

        Se nenhuma coleção for fornecida, embaralha o próprio baralho.

        Args:
            cards: Coleção de cartas a ser embaralhada.
        """
        if cards is None:
            cards = self.cards

        random.shuffle(cards)
