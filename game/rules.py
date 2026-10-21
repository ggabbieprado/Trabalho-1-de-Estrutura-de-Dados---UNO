from models.card import Card, CardType, Color


class Rules:

    @staticmethod
    def can_play(card: Card, top_card: Card, current_color: Color) -> bool:
        """
        Verifica se uma carta pode ser jogada sobre a carta atual.

        Uma carta pode ser jogada quando:
        - é um coringa;
        - possui a mesma cor da cor atualmente válida;
        - possui o mesmo tipo da carta no topo do descarte;
        - é uma carta numérica com o mesmo valor da carta no topo.

        Args:
            card: Carta que o jogador deseja jogar.
            top_card: Carta atualmente no topo do descarte.
            current_color: Cor atualmente válida para a jogada.

        Returns:
            True se a carta puder ser jogada; False caso contrário.
        """
        if card.color == Color.WILD:
            return True

        if card.color == current_color:
            return True

        if (card.type != CardType.NUMBER and card.type == top_card.type):
            return True

        if (card.type == CardType.NUMBER and top_card.type == CardType.NUMBER
            and card.value == top_card.value):
            return True

        return False
