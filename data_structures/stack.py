from typing import Generic, TypeVar

T = TypeVar("T")


class _Node(Generic[T]):
    def __init__(self, data: T, next_node: "_Node[T] | None" = None) -> None:
        self.data = data
        self.next = next_node


class Stack(Generic[T]):
    """
    Estrutura de dados do tipo Pilha (LIFO).

    O último elemento inserido é o primeiro a ser removido.

    ATENÇÃO:
        Não utilize a classe `list` do Python para implementar a pilha.

        A estrutura deve ser implementada utilizando a classe Arranjo
        (implementação de arranjo estático) ou encadeamento.

        A Stack não deve ter uma capacidade máxima. Ela deve poder
        crescer conforme novos elementos forem inseridos.
    """

    def __init__(self) -> None:
        self._top: _Node[T] | None = None
        self._size = 0

    def push(self, item: T) -> None:
        self._top = _Node(item, self._top)
        self._size += 1

    def pop(self) -> T:
        if self._top is None:
            raise IndexError("Não é possível remover de uma pilha vazia.")

        item = self._top.data
        self._top = self._top.next
        self._size -= 1
        return item

    def peek(self) -> T:
        if self._top is None:
            raise IndexError("Não é possível consultar uma pilha vazia.")
        return self._top.data

    def is_empty(self) -> bool:
        return self._top is None

    def size(self) -> int:
        return self._size

    def __len__(self) -> int:
        return self._size
