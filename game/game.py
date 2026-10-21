from models.card import Card, CardType, Color
from models.deck import Deck
from models.player import Player

from game.rules import Rules
from game.turn import TurnManager

from data_structures.circular_list import CircularList

from ui.terminal import TerminalUI


class Game:
    """
    Controla uma partida de UNO.

    É responsável por coordenar os componentes do jogo,
    controlar o fluxo da partida e aplicar as regras.

    As estruturas de dados utilizadas pelo jogo
    são fornecidas externamente.
    """

    def __init__(self, players: CircularList[Player],
        draw_pile, discard_pile) -> None:
        """
        Inicializa uma partida.

        Args:
            players: Lista circular contendo os jogadores.
            draw_pile: Pilha utilizada como monte de compra.
            discard_pile: Pilha utilizada como monte de descarte.

        Raises:
            ValueError: Se houver menos de dois jogadores.
        """
        if len(players) < 2:
            raise ValueError("É necessário ter pelo menos dois jogadores.")

        self.players = players
        self.draw_pile = draw_pile
        self.discard_pile = discard_pile

        self.deck = Deck()

        self.current_color: Color | None = None
        self.turn_manager: TurnManager | None = None

    def setup(self) -> None:
        """
        Prepara a partida antes do primeiro turno.

        Distribui as cartas aos jogadores e inicia
        os montes de compra e descarte.
        """
        for card in self.deck.cards:
            self.draw_pile.push(card)

        self._deal_cards()
        self._start_discard_pile()

        self.turn_manager = TurnManager(self.players)

    def _deal_cards(self, amount: int = 7) -> None:
        """
        Distribui cartas aos jogadores.

        Args:
            amount: Quantidade de cartas que cada jogador recebe.
        """
        for _ in range(amount):
            for player in self.players:
                player.receive(self._draw_card())

    def _start_discard_pile(self) -> None:
        """
        Coloca a primeira carta no monte de descarte.

        A carta inicial não pode ser um coringa de +4.
        """
        wild_cards = []
        card = self._draw_card()

        while card.type in (CardType.WILD, CardType.WILD_DRAW_FOUR):
            wild_cards.append(card)
            card = self._draw_card()

        self.discard_pile.push(card)
        self.current_color = card.color

        for wild_card in wild_cards:
            self.draw_pile.push(wild_card)


    def _draw_card(self) -> Card:
        """
        Retira uma carta do topo do monte de compra.
        Se o monte estiver vazio, recicla o descarte.

        Returns:
            A carta retirada do monte de compra.

        Raises:
            RuntimeError: Se não houver cartas disponíveis.
        """
        if self.draw_pile.is_empty():
            self._recycle_discard()

        if self.draw_pile.is_empty():
            raise RuntimeError("Não há cartas disponíveis para compra.")

        return self.draw_pile.pop()

    def _recycle_discard(self) -> None:
        """
        Recria o monte de compra utilizando o descarte.
        A carta no topo do descarte permanece no jogo.
        """
        if self.discard_pile.size() <= 1:
            return

        top_card = self.discard_pile.pop()

        cards = []

        while not self.discard_pile.is_empty():
            cards.append(self.discard_pile.pop())

        self.deck.shuffle(cards)

        for card in cards:
            self.draw_pile.push(card)

        self.discard_pile.push(top_card)

    def _valid_cards(self, player: Player) -> list[int]:
        """
        Obtém os índices das cartas que o jogador pode jogar.

        Args:
            player: Jogador que está realizando a jogada.

        Returns:
            Lista contendo os índices das cartas válidas.
        """
        if self.current_color is None:
            return []

        top_card = self.discard_pile.peek()

        valid = []

        for index, card in enumerate(player.hand):
            if Rules.can_play(card, top_card, self.current_color):
                valid.append(index)

        return valid

    def _play_card(self, player: Player, index: int) -> Card:
        """
        Joga uma carta da mão do jogador.

        Args:
            player: Jogador que está realizando a jogada.
            index: Índice da carta na mão.
        
        Return:
            A carta que foi descartada no monte
        """
        card = player.remove_card(index)

        self.discard_pile.push(card)

        if card.type in (CardType.WILD, CardType.WILD_DRAW_FOUR):
            self.current_color = TerminalUI.choose_color()
        else:
            self.current_color = card.color

        return card



    def _draw_for_player(self, player: Player, amount: int = 1) -> list[Card]:
        """
        Faz o jogador comprar uma quantidade de cartas.

        Args:
            player: Jogador que receberá as cartas.
            amount: Quantidade de cartas a comprar.

        Returns:
            Lista das cartas compradas.
        """
        drawn_cards = []

        for _ in range(amount):
            card = self._draw_card()
            player.receive(card)
            drawn_cards.append(card)

        return drawn_cards


    def _has_won(self, player: Player) -> bool:
        """
        Verifica se um jogador venceu a partida.

        Args:
            player: Jogador a ser verificado.

        Returns:
            True se o jogador não possuir mais cartas.
        """
        return player.has_won()


    def run(self) -> None:
        TerminalUI.clear()
        TerminalUI.title()

        self.setup()

        TerminalUI.show_message("A partida começou!")

        while True:
            if self.play_turn():
                winner = self.turn_manager.current()

                TerminalUI.clear()
                TerminalUI.show_message(f"🎉 {winner.name} venceu a partida!")
                break


    def play_turn(self) -> bool:
        """
        Executa o turno do jogador atual.

        Returns:
            True se a partida terminou; False caso contrário.
        """
        if self.turn_manager is None:
            raise RuntimeError("A partida não foi iniciada.")

        player = self.turn_manager.current()

        TerminalUI.clear()
        TerminalUI.show_top_card(self.discard_pile.peek())

        valid_indexes = self._valid_cards(player)

        TerminalUI.show_player_hand(player, self.current_color, valid_indexes)

        choice = TerminalUI.choose_card(valid_indexes)

        played_card = None

        if choice is not None:
            played_card = self._play_card(player, choice)

            if self._has_won(player):
                return True
        else: 
            drawn_cards = self._draw_for_player(player)
            drawn_card = drawn_cards[0]

            drawn_index = player.hand.find(drawn_card)

            if Rules.can_play(drawn_card, self.discard_pile.peek(), 
                              self.current_color):
                choice = TerminalUI.read_yes_no(
                    f"A carta comprada ({drawn_card}) pode ser jogada." 
                    "Deseja usá-la? [S/N]: "
                )

                if choice:
                    played_card = self._play_card(player, drawn_index)


        if played_card is not None:
            if played_card.type == CardType.REVERSE:
                self.turn_manager.reverse()

            elif played_card.type == CardType.SKIP:
                self.turn_manager.next()

            elif played_card.type == CardType.DRAW_TWO:
                self.turn_manager.next()
                self._draw_for_player(self.turn_manager.current(), 2)

            elif played_card.type == CardType.WILD_DRAW_FOUR:
                self.turn_manager.next()
                self._draw_for_player(self.turn_manager.current(), 4)
            
        self.turn_manager.next()

        return False