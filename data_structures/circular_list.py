from typing import Generic, Iterator, TypeVar

T = TypeVar("T")

class Node(Generic[T]):
    """
    Nó de uma lista circular.

    Cada nó possui uma referência para o próximo nó e para o nó
    anterior. A lista deve ser construída utilizando objetos desta
    classe.

    Não utilize a classe `list` do Python para implementar a lista.
    """
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.next: Node[T] | None = None
        self.previous: Node[T] | None = None


class CircularList(Generic[T]):
    """
    Estrutura de dados de lista duplamente ligada e circular.

    Mantém uma referência para o elemento atualmente selecionado.

    A implementação da lista deve utilizar a classe Node definida
    acima. Não utilize a classe `list` do Python.

    A lista deve ser circular e duplamente ligada, ou seja:

        - O último nó deve apontar para o primeiro nó através de `next`.
        - O primeiro nó deve apontar para o último nó através de
        `previous`.
        - Cada nó deve manter referências para seu próximo e seu
        elemento anterior.
    """

    def __init__(self) -> None:
        """
        Inicializa uma lista circular vazia.

        A implementação deve utilizar a classe Node.

        Não utilize `list` do Python.
        """
        self._current: Node[T] | None = None
        self._size = 0

    def add(self, data: T) -> None:
        """
        Adiciona um elemento ao final da lista.

        Args:
            data: Elemento a ser adicionado.

        Exemplo:
            >>> lista = CircularList[int]()
            >>> lista.add(10)
            >>> lista.add(20)
            >>> lista.current()
            10
            >>> lista.size()
            2
        """
        new_node = Node(data)
        if self._current is None:
            new_node.next = new_node
            new_node.previous = new_node
            self._current = new_node
        else:
            last = self._current.previous
            assert last is not None
            new_node.next = self._current
            new_node.previous = last
            last.next = new_node
            self._current.previous = new_node
        self._size += 1

    def current(self) -> T:
        """
        Retorna o elemento atualmente selecionado.

        Returns:
            Elemento atual.

        Raises:
            IndexError: Se a lista estiver vazia.

        Exemplo:
            >>> lista = CircularList[str]()
            >>> lista.add("a")
            >>> lista.add("b")
            >>> lista.current()
            'a'
        """
        if self._current is None:
            raise IndexError("A lista circular está vazia.")
        return self._current.data

    def move_next(self) -> T:
        """
        Avança para o próximo elemento.

        Como a lista é circular, ao avançar a partir do último
        elemento, o primeiro elemento passa a ser o atual.

        Returns:
            O novo elemento atual.

        Raises:
            IndexError: Se a lista estiver vazia.

        Exemplo:
            >>> lista = CircularList[int]()
            >>> lista.add(10)
            >>> lista.add(20)
            >>> lista.add(30)
            >>> lista.move_next()
            20
            >>> lista.move_next()
            30
            >>> lista.move_next()
            10
        """
        if self._current is None:
            raise IndexError("A lista circular está vazia.")
        assert self._current.next is not None
        self._current = self._current.next
        return self._current.data

    def move_previous(self) -> T:
        """
        Retrocede para o elemento anterior.

        Como a lista é circular, ao retroceder a partir do primeiro
        elemento, o último elemento passa a ser o atual.

        Returns:
            O novo elemento atual.

        Raises:
            IndexError: Se a lista estiver vazia.

        Exemplo:
            >>> lista = CircularList[int]()
            >>> lista.add(10)
            >>> lista.add(20)
            >>> lista.add(30)
            >>> lista.move_previous()
            30
            >>> lista.move_previous()
            20
        """
        if self._current is None:
            raise IndexError("A lista circular está vazia.")
        assert self._current.previous is not None
        self._current = self._current.previous
        return self._current.data

    def peek(self, offset: int = 1) -> T:
        """
        Retorna um elemento a uma determinada distância do atual sem
        alterar o elemento atualmente selecionado.

        Args:
            offset: Quantidade de posições a avançar. Valores positivos
                percorrem a lista através de `next`; valores negativos
                percorrem a lista através de `previous`.

        Returns:
            O elemento encontrado.

        Raises:
            IndexError: Se a lista estiver vazia.

        Exemplos:
            >>> lista = CircularList[int]()
            >>> lista.add(10)
            >>> lista.add(20)
            >>> lista.add(30)
            >>> lista.current()
            10
            >>> lista.peek(1)
            20
            >>> lista.current()
            10
            >>> lista.peek(2)
            30
            >>> lista.peek(3)
            10
            >>> lista.peek(-1)
            30
        """
        if self._current is None:
            raise IndexError("A lista circular está vazia.")

        node = self._current
        if offset >= 0:
            for _ in range(offset):
                assert node.next is not None
                node = node.next
        else:
            for _ in range(-offset):
                assert node.previous is not None
                node = node.previous
        return node.data

    def size(self) -> int:
        """
        Retorna a quantidade de elementos.

        Returns:
            Número de elementos da lista.

        Exemplo:
            >>> lista = CircularList[int]()
            >>> lista.add(10)
            >>> lista.add(20)
            >>> lista.size()
            2
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Verifica se a lista está vazia.

        Returns:
            True se estiver vazia; False caso contrário.

        Exemplos:
            >>> lista = CircularList[int]()
            >>> lista.is_empty()
            True
            >>> lista.add(10)
            >>> lista.is_empty()
            False
        """
        return self._size == 0

    def __len__(self) -> int:
        """
        Retorna a quantidade de elementos.

        Exemplo:
            >>> lista = CircularList[int]()
            >>> lista.add(10)
            >>> lista.add(20)
            >>> len(lista)
            2
        """
        return self._size

    def __iter__(self) -> Iterator[T]:
        """
        Percorre todos os elementos da lista uma única vez.

        Como a lista é circular, a iteração deve terminar após visitar
        exatamente `_size` elementos.

        Exemplo:
            >>> lista = CircularList[int]()
            >>> lista.add(10)
            >>> lista.add(20)
            >>> lista.add(30)
            >>> list(lista)
            [10, 20, 30]
        """

        if self._current is None:
            return

        current = self._current
        for _ in range(self._size):
            yield current.data
            assert current.next is not None
            current = current.next
