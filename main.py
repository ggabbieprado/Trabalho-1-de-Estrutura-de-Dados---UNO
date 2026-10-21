from data_structures.circular_list import CircularList
from data_structures.linked_list import LinkedList
from data_structures.stack import Stack

from game.game import Game
from models.player import Player
from ui.terminal import TerminalUI


def main() -> None:
    """
    Cria e inicia uma partida de UNO.
    """
    TerminalUI.title()
    TerminalUI.show_message("Configuração da partida")

    number_of_players = TerminalUI.read_number(
        "Quantidade de jogadores (2-6): ",
        minimum=2,
        maximum=6,
    )

    players = CircularList()

    for number in range(1, number_of_players + 1):
        name = TerminalUI.read_text(
            f"Nome do jogador {number}: "
        )

        player = Player(name, LinkedList())
        players.add(player)

    draw_pile = Stack()
    discard_pile = Stack()

    game = Game(
        players,
        draw_pile,
        discard_pile,
    )

    game.run()


if __name__ == "__main__":
    main()
