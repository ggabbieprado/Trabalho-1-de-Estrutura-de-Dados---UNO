from typing import Generic, TypeVar

from arranjo import Arranjo


T = TypeVar("T")


class Pilha(Generic[T]):
    """
    Representa uma Pilha implementada utilizando um arranjo estático.

    A Pilha segue o princípio LIFO (Last In, First Out): o último
    elemento inserido é o primeiro elemento que pode ser removido.
    """

    __dados: Arranjo[T]
    __topo: int

    def __init__(self, capacidade: int) -> None:
        """
        Cria uma Pilha vazia com a capacidade informada.

        Parâmetros
        ----------
        capacidade
            Número máximo de elementos que a Pilha pode armazenar.

        Pré-condição
        ------------
        ``capacidade > 0``

        Pós-condição
        ------------
        A Pilha está vazia e possui a capacidade informada.

        Exemplos
        --------
        >>> p = Pilha[int](5)
        >>> p.is_empty()
        True
        >>> p.is_full()
        False
        """
        self.__dados = Arranjo[T](capacidade)
        self.__topo = -1

    def is_empty(self) -> bool:
        """
        Verifica se a Pilha está vazia.

        Retorna
        -------
        bool
            ``True`` se a Pilha estiver vazia e ``False`` caso contrário.

        Pós-condição
        ------------
        O estado da Pilha permanece inalterado.

        Exemplos
        --------
        >>> p = Pilha[int](3)
        >>> p.is_empty()
        True

        >>> p.push(10)
        >>> p.is_empty()
        False
        """
        pass

    def is_full(self) -> bool:
        """
        Verifica se a Pilha está cheia.

        Retorna
        -------
        bool
            ``True`` se a Pilha estiver cheia e ``False`` caso contrário.

        Pós-condição
        ------------
        O estado da Pilha permanece inalterado.

        Exemplos
        --------
        >>> p = Pilha[int](2)
        >>> p.is_full()
        False

        >>> p.push(10)
        >>> p.push(20)
        >>> p.is_full()
        True
        """
        pass

    def push(self, elemento: T) -> None:
        """
        Insere ``elemento`` no topo da Pilha.

        Parâmetros
        ----------
        elemento
            Elemento a ser inserido.

        Pré-condição
        ------------
        A Pilha não está cheia.

        Pós-condição
        ------------
        ``elemento`` passa a ocupar o topo da Pilha.
        A quantidade de elementos aumenta em uma unidade.

        Levanta
        -------
        OverflowError
            Se a Pilha estiver cheia.

        Exemplos
        --------
        >>> p = Pilha[str](3)
        >>> p.push("A")
        >>> p.push("B")
        >>> p.top()
        'B'

        >>> p.push("C")
        >>> p.is_full()
        True

        >>> p.push("D")
        Traceback (most recent call last):
        ...
        OverflowError: pilha cheia
        """
        pass

    def pop(self) -> T:
        """
        Remove e retorna o elemento que está no topo da Pilha.

        Retorna
        -------
        T
            Elemento removido.

        Pré-condição
        ------------
        A Pilha não está vazia.

        Pós-condição
        ------------
        O elemento que estava no topo é removido.
        A quantidade de elementos diminui em uma unidade.

        Levanta
        -------
        IndexError
            Se a Pilha estiver vazia.

        Exemplos
        --------
        >>> p = Pilha[int](3)
        >>> p.push(10)
        >>> p.push(20)
        >>> p.pop()
        20
        >>> p.pop()
        10
        >>> p.is_empty()
        True

        >>> p.pop()
        Traceback (most recent call last):
        ...
        IndexError: pilha vazia
        """
        pass

    def top(self) -> T:
        """
        Retorna o elemento que está no topo da Pilha sem removê-lo.

        Retorna
        -------
        T
            Elemento que está no topo.

        Pré-condição
        ------------
        A Pilha não está vazia.

        Pós-condição
        ------------
        O estado da Pilha permanece inalterado.

        Levanta
        -------
        IndexError
            Se a Pilha estiver vazia.

        Exemplos
        --------
        >>> p = Pilha[int](3)
        >>> p.push(10)
        >>> p.push(20)
        >>> p.top()
        20
        >>> p.top()
        20
        >>> p.pop()
        20

        >>> p = Pilha[int](3)
        >>> p.top()
        Traceback (most recent call last):
        ...
        IndexError: pilha vazia
        """
        pass