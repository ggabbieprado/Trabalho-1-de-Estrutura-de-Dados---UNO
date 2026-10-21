from __future__ import annotations

from typing import Generic, Iterator, TypeVar


T = TypeVar("T")


class Node(Generic[T]):
    """
    Nó de uma lista ligada.

    Cada nó armazena um elemento do tipo T e uma referência para o
    próximo nó.

    ATENÇÃO:
        A classe Node deve ser utilizada para implementar a LinkedList.
        Não utilize a classe `list` do Python.
    """

    def __init__(self, data: T):
        self.data: T = data
        self.next: Node[T] | None = None


class LinkedList(Generic[T]):
    """
    Estrutura de dados de lista ligada simples.

    A implementação da lista deve utilizar a classe Node definida acima.

    ATENÇÃO:
        Não utilize a classe `list` do Python para implementar a lista.

        Cada elemento da lista deve ser armazenado em um objeto Node.
        A lista deve manter uma referência para o primeiro nó (head)
        e a quantidade de elementos (_size).
    """

    def __init__(self):
        """
        Inicializa uma lista vazia.

        A implementação deve utilizar a classe Node.

        Não utilize `list` do Python.
        """
        self.head: Node[T] | None = None
        self._size = 0

    def add(self, data: T) -> None:
        """
        Adiciona um elemento ao final da lista.

        Args:
            data: Elemento a ser adicionado.

        Exemplo:
            >>> lista = LinkedList[int]()
            >>> lista.add(10)
            >>> lista.add(20)
            >>> lista.get(1)
            20
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._size += 1

    def remove(self, index: int) -> T:
        """
        Remove e retorna o elemento de uma posição.

        Args:
            index: Índice do elemento.

        Returns:
            O elemento removido.

        Raises:
            IndexError: Se o índice for inválido.

        Exemplos:
            >>> lista = LinkedList[int]()
            >>> lista.add(10)
            >>> lista.add(20)
            >>> lista.add(30)
            >>> lista.remove(1)
            20
            >>> lista.get(1)
            30

            >>> lista.remove(0)
            10
        """
        if index < 0 or index >= self._size:
            raise IndexError("Índice fora dos limites da lista.")

        if index == 0:
            assert self.head is not None
            removed = self.head
            self.head = removed.next
        else:
            previous = self.head
            for _ in range(index - 1):
                assert previous is not None
                previous = previous.next
            assert previous is not None and previous.next is not None
            removed = previous.next
            previous.next = removed.next

        self._size -= 1
        return removed.data

    def get(self, index: int) -> T:
        """
        Retorna o elemento de uma posição sem removê-lo.

        Args:
            index: Índice do elemento.

        Returns:
            O elemento encontrado.

        Raises:
            IndexError: Se o índice for inválido.

        Exemplos:
            >>> lista = LinkedList[int]()
            >>> lista.add(10)
            >>> lista.add(20)
            >>> lista.get(0)
            10
            >>> lista.get(1)
            20
        """
        if index < 0 or index >= self._size:
            raise IndexError("Índice fora dos limites da lista.")

        current = self.head
        for _ in range(index):
            assert current is not None
            current = current.next
        assert current is not None
        return current.data

    def find(self, data: T) -> int:
        """
        Devolve o índice do elemento na lista, ou -1 caso não encontre.

        Args:
            data: Elemento a ser procurado.

        Returns:
            O índice da primeira ocorrência do elemento ou -1 caso o
            elemento não esteja na lista.

        Exemplos:
            >>> lista = LinkedList[str]()
            >>> lista.add("a")
            >>> lista.add("b")
            >>> lista.add("c")
            >>> lista.find("b")
            1
            >>> lista.find("x")
            -1
        """
        current = self.head
        index = 0
        while current is not None:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def size(self) -> int:
        """
        Retorna a quantidade de elementos.

        Returns:
            Número de elementos.

        Exemplo:
            >>> lista = LinkedList[int]()
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
            >>> lista = LinkedList[int]()
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
            >>> lista = LinkedList[int]()
            >>> lista.add(10)
            >>> lista.add(20)
            >>> len(lista)
            2
        """
        return self._size

    def __iter__(self) -> Iterator[T]:
        """
        Permite percorrer a lista com for.

        Exemplo:
            >>> lista = LinkedList[int]()
            >>> lista.add(10)
            >>> lista.add(20)
            >>> lista.add(30)
            >>> list(lista)
            [10, 20, 30]
        """
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

