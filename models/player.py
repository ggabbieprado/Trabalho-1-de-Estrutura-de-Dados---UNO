from typing import Iterable

from models.card import Card
from data_structures.linked_list import LinkedList


class Player:
    def __init__(self, name: str, hand: LinkedList[Card]):
        self.name: str = name
        self.hand: LinkedList[Card] = hand

    def receive(self, card: Card) -> None:
        """Adiciona uma carta à mão do jogador."""
        self.hand.add(card)

    def receive_many(self, cards: Iterable[Card]) -> None:
        """Adiciona várias cartas à mão do jogador."""
        for card in cards:
            self.receive(card)

    def remove_card(self, index: int) -> Card:
        """Remove e retorna uma carta da mão."""
        return self.hand.remove(index)

    def has_won(self) -> bool:
        """Retorna True se o jogador não possui cartas."""
        return self.hand.is_empty()

    def __str__(self) -> str:
        """Retorna o nome do jogador."""
        return self.name
