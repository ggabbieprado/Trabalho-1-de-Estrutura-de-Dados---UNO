from data_structures.circular_list import CircularList
from models.player import Player


class TurnManager:
    """
    Gerencia a ordem dos turnos dos jogadores.

    A ordem dos jogadores é mantida por uma CircularList.
    """

    def __init__(self, players: CircularList[Player]) -> None:
        """
        Inicializa o gerenciador de turnos.

        Args:
            players: Lista circular contendo os jogadores.

        Raises:
            ValueError: Se a lista de jogadores estiver vazia.
        """
        if len(players) == 0:
            raise ValueError("É necessário ter pelo menos um jogador.")

        self.players = players
        self.direction = 1  # 1 = sentido horário, -1 = sentido anti-horário

    def current(self) -> Player:
        """
        Retorna o jogador que possui o turno atual.

        Returns:
            O jogador atual.
        """
        return self.players.current()

    def next(self) -> Player:
        """
        Avança o turno para o próximo jogador, respeitando a direção atual.

        Returns:
            O jogador que passa a ter o turno.
        """
        if self.direction == 1:
            return self.players.move_next()
        return self.players.move_previous()

    def peek_next(self) -> Player:
        """
        Apenas consulta o próximo jogador, respeitando a direção atual.

        Returns:
            O jogador que jogaria em seguida.
        """
        return self.players.peek(self.direction)

    def previous(self) -> Player:
        """
        Retorna o turno para o jogador anterior, respeitando a direção atual.

        Returns:
            O jogador que passa a ter o turno.
        """
        if self.direction == 1:
            return self.players.move_previous()
        return self.players.move_next()

    def reverse(self) -> None:
        """
        Inverte a direção dos turnos.
        """
        self.direction *= -1


    def advance(self, amount: int = 1) -> Player:
        """
        Avança o turno uma quantidade determinada de jogadores.

        Args:
            amount: Quantidade de posições a avançar.

        Returns:
            O jogador que passa a ter o turno.

        Raises:
            ValueError: Se amount for negativo.
        """
        if amount < 0:
            raise ValueError("A quantidade deve ser não negativa.")
        for _ in range(amount):
            self.next()
        return self.current()
