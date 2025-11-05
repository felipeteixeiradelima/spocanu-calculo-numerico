import numpy as np
from numpy.typing import NDArray

from exceptions import OrdemInvalidaError

n: int
b: NDArray

def obter_ordem() -> int:
    print("ENTRADA DA ORDEM DA MATRIZ M")

    while True:
        n_input = input("Digite a ordem da matriz: ")

        try:
            n_int = int(n_input)
            if n_int <= 0:
                raise OrdemInvalidaError(f"Ordem menor ou igual a 0: '{n_int}'")

            return n_int

        except ValueError as e:
            print(f'Valor inválido: "{e}"!\n')

        except OrdemInvalidaError as e:
            print(f'Ordem inválida: "{e}"!\n')

def obter_vetor_b() -> NDArray:
    ordem = n

    b_local = np.empty(ordem)

    print("\nENTRADA DO VETOR B")

    for i in range(ordem):
        while True:
            valor_input = input(f"Digite o {i+1}º elemento de b: ")

            try:
                b_local[i] = int(valor_input)
                break

            except ValueError as e:
                print(f'Valor inválido: "{e}"!\n')
    
    return b_local


if __name__ == "__main__":
    n = obter_ordem()

    b = obter_vetor_b()
