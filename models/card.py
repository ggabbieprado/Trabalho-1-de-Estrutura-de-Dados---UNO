from dataclasses import dataclass
from enum import Enum

class Color(Enum):
    RED = ("Vermelho", "🔴")
    BLUE = ("Azul", "🔵")
    GREEN = ("Verde", "🟢")
    YELLOW = ("Amarelo", "🟡")
    WILD = ("Coringa", "🃏")

    @property
    def name_pt(self):
        return self.value[0]

    @property
    def symbol(self):
        return self.value[1]


class CardType(Enum):
    NUMBER = "Número"
    SKIP = "Bloqueio"
    REVERSE = "Inverter"
    DRAW_TWO = "+2"
    WILD = "Coringa"
    WILD_DRAW_FOUR = "+4"


@dataclass(frozen=True)
class Card:
    color: Color
    type: CardType
    value: int | None = None

    def __str__(self):
        if self.type == CardType.NUMBER:
            return f"{self.color.symbol} {self.value}"
        return f"{self.color.symbol} {self.type.value}"

