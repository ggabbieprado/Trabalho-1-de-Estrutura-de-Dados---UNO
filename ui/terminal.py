from models.card import Card, Color
from models.player import Player


class TerminalUI:
    """
    Interface de usuário baseada no terminal.

    Responsável pela entrada e saída de dados do jogo.
    Não contém lógica relacionada às regras do UNO.
    """

    @staticmethod
    def clear() -> None:
        """
        Limpa visualmente o terminal.
        """
        print("\n" * 3)

    @staticmethod
    def title() -> None:
        """
        Exibe o título do jogo.
        """
        print("=" * 60)
        print("                         UNO")
        print("=" * 60)

    @staticmethod
    def show_player_hand(player: Player, current_color: Color,
                         valid_indexes: list[int]) -> None:
        """
        Exibe a mão do jogador, destacando as cartas que podem
        ser jogadas.

        Args:
            player: Jogador cuja mão será exibida.
            current_color: Cor atualmente válida para a jogada.
            valid_indexes: Indices das cartas que podem ser escolhidas
        """
        print()
        print(f"Jogador: {player.name}")
        print(
            f"Cor atual: "
            f"{current_color.name_pt} {current_color.symbol}"
        )
        print()
        print("Sua mão:")

        for index, card in enumerate(player.hand):
            marker = "✓" if index in valid_indexes else " "

            print(f"  [{index + 1}] {marker} {card}")

        print()

    @staticmethod
    def show_top_card(card: Card) -> None:
        """
        Exibe a carta no topo do monte de descarte.

        Args:
            card: Carta que será exibida.
        """
        print()
        print(f"Carta no descarte: {card}")
        print()

    @staticmethod
    def choose_card(valid_indexes: list[int]) -> int | None:
        """
        Solicita ao jogador a escolha de uma carta.

        O jogador pode escolher uma carta válida ou optar
        por comprar uma carta.

        Args:
            valid_indexes: Índices das cartas que podem ser jogadas.

        Returns:
            O índice da carta escolhida, ou None caso o jogador
            escolha comprar uma carta.
        """
        while True:
            answer = input(
                "Escolha uma carta ou [D] para comprar: "
            ).strip().lower()

            if answer == "d":
                return None

            try:
                index = int(answer) - 1
            except ValueError:
                print("Digite um número válido.")
                continue

            if index not in valid_indexes:
                print("Essa carta não pode ser jogada.")
                continue

            return index

    @staticmethod
    def choose_color() -> Color:
        """
        Solicita ao jogador a escolha de uma cor.

        Returns:
            A cor escolhida pelo jogador.
        """
        colors = [
            Color.RED,
            Color.BLUE,
            Color.GREEN,
            Color.YELLOW,
        ]

        print()
        print("Escolha a nova cor:")

        for index, color in enumerate(colors, start=1):
            print(
                f"  [{index}] "
                f"{color.name_pt} {color.symbol}"
            )

        return colors[
            TerminalUI.read_number("> ", minimum=1, maximum=len(colors)) - 1
        ]

    @staticmethod
    def read_number(prompt: str, minimum: int | None = None,
                    maximum: int | None = None) -> int:
        """
        Solicita um número inteiro ao usuário.

        Args:
            prompt: Mensagem exibida antes da leitura.
            minimum: Valor mínimo aceito, se houver.
            maximum: Valor máximo aceito, se houver.

        Returns:
            O número inteiro informado pelo usuário.
        """
        while True:
            try:
                value = int(input(prompt))

                if minimum is not None and value < minimum:
                    print(
                        f"Digite um valor maior ou igual a {minimum}."
                    )
                    continue

                if maximum is not None and value > maximum:
                    print(
                        f"Digite um valor menor ou igual a {maximum}."
                    )
                    continue

                return value

            except ValueError:
                print("Digite um número inteiro válido.")

    @staticmethod
    def read_text(prompt: str) -> str:
        """
        Solicita um texto ao usuário.

        A entrada é removida de espaços no início e no final.

        Args:
            prompt: Mensagem exibida antes da leitura.

        Returns:
            Texto informado pelo usuário.
        """
        while True:
            value = input(prompt).strip()

            if value:
                return value

            print("O texto não pode estar vazio.")

    @staticmethod
    def read_yes_no(prompt: str) -> bool:
        """
        Solicita uma resposta de sim ou não.

        Aceita 's', 'sim', 'n' e 'nao' (ou 'não').

        Args:
            prompt: Mensagem exibida antes da leitura.

        Returns:
            True para uma resposta afirmativa e False para uma
            resposta negativa.
        """
        while True:
            value = input(prompt).strip().lower()

            if value in ("s", "sim"):
                return True

            if value in ("n", "nao", "não"):
                return False

            print("Responda com S ou N.")

    @staticmethod
    def show_message(message: str) -> None:
        """
        Exibe uma mensagem no terminal.

        Args:
            message: Texto que será exibido.
        """
        print()
        print(message)
        print()

    @staticmethod
    def pause() -> None:
        """
        Aguarda o usuário pressionar ENTER para continuar.
        """
        input("Pressione ENTER para continuar...")
