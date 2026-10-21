from typing import Generic, TypeVar

T = TypeVar("T")


class Arranjo(Generic[T]):
    """
    Representa um arranjo estático.

    A representação interna utiliza uma lista de tamanho fixo.
    """

    __elementos: list[T | None]

    def __init__(self, capacidade: int) -> None:
        """
        Cria um arranjo com a ``capacidade`` informada.

        Pré-condição
        ------------
        ``capacidade > 0``

        Pós-condição
        ------------
        O arranjo possui ``capacidade`` posições, todas inicialmente
        preenchidas com ``None``.

        Levanta
        -------
        ValueError
            Se a capacidade for menor ou igual a zero.

        Exemplos
        --------
        >>> a = Arranjo[int](5)
        >>> len(a)
        5

        >>> Arranjo[int](0)
        Traceback (most recent call last):
        ...
        ValueError: a capacidade deve ser maior que zero
        """
        if capacidade <= 0:
            raise ValueError("a capacidade deve ser maior que zero")

        self.__elementos = [None] * capacidade

    def __len__(self) -> int:
        """
        Devolve a capacidade do arranjo.

        Exemplos
        --------
        >>> a = Arranjo[int](5)
        >>> len(a)
        5
        """
        return len(self.__elementos)

    def __getitem__(self, indice: int) -> T | None:
        """
        Devolve o elemento armazenado na posição indicada por ``indice``.

        Pré-condição
        ------------
        ``0 <= indice < len(self)``

        Pós-condição
        ------------
        O arranjo permanece inalterado.

        Levanta
        -------
        IndexError
            Se ``indice`` estiver fora dos limites do arranjo.

        Exemplos
        --------
        >>> a = Arranjo[str](3)
        >>> a[1] = "A"
        >>> a[1]
        'A'

        >>> a[-1]
        Traceback (most recent call last):
        ...
        IndexError: índice fora dos limites do arranjo

        >>> a[3]
        Traceback (most recent call last):
        ...
        IndexError: índice fora dos limites do arranjo
        """
        if not 0 <= indice < len(self):
            raise IndexError("índice fora dos limites do arranjo")

        return self.__elementos[indice]

    def __setitem__(self, indice: int, valor: T) -> None:
        """
        Armazena ``valor`` na posição indicada por ``indice``.

        Pré-condição
        ------------
        ``0 <= indice < len(self)``

        Pós-condição
        ------------
        A posição ``indice`` passa a armazenar ``valor``.

        Levanta
        -------
        IndexError
            Se ``indice`` estiver fora dos limites do arranjo.

        Exemplos
        --------
        >>> a = Arranjo[int](2)
        >>> a[0] = 10
        >>> a[0]
        10

        >>> a[2] = 20
        Traceback (most recent call last):
        ...
        IndexError: índice fora dos limites do arranjo

        >>> a[-1] = 20
        Traceback (most recent call last):
        ...
        IndexError: índice fora dos limites do arranjo
        """
        if not 0 <= indice < len(self):
            raise IndexError("índice fora dos limites do arranjo")

        self.__elementos[indice] = valor

    def __str__(self) -> str:
        """
        Devolve uma representação textual dos elementos do arranjo.

        Exemplos
        --------
        >>> a = Arranjo[int](3)
        >>> a[0] = 10
        >>> str(a)
        '[10, None, None]'
        """
        return str(self.__elementos)