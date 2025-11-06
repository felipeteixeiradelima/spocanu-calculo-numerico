import numpy as np
from numpy import float64
from numpy.typing import NDArray

from exceptions import MatrizInvalidaError

def _validar_matriz_gauss_jacobi(matriz: NDArray[float64]) -> None:
    n = matriz.shape[0]

    for i in range(n):
        if matriz[i,i] == 0:
            raise MatrizInvalidaError(f"Elemento na posição ({i},{i}) é igual a 0")

def _proxima_iteracao_gauss_jacobi(matriz: NDArray[float64],
                                   vetor_b: NDArray[float64],
                                   vetor_x: NDArray[float64]) -> NDArray[float64]:
    
    _validar_matriz_gauss_jacobi(matriz)

    n = matriz.shape[0]

    novo_vetor_x = np.empty(n)

    for i in range(n):
        soma = 0
        for j in range(n):
            if i == j:
                continue

            soma += matriz[i,j] * vetor_x[j]

        novo_vetor_x[i] = (vetor_b[i] - soma) / matriz[i,i]

    return novo_vetor_x

def _calcular_diferenca_relativa_gauss_jacobi(vetor_x: NDArray[float64], novo_vetor_x: NDArray[float64]) -> float:
    dividendo = max(abs(novo_vetor_x - vetor_x))
    divisor = max(abs(vetor_x))

    if divisor == 0:
        return 1

    return dividendo/divisor

def gauss_jacobi(matriz: NDArray[float64],
                 vetor_b: NDArray[float64]) -> NDArray[float64]:

    n = matriz.shape[0]

    tolerancia = 0.001
    diferenca_relativa = 1

    vetor_x = np.zeros(n)

    while diferenca_relativa >= tolerancia:
        novo_vetor_x = _proxima_iteracao_gauss_jacobi(matriz, vetor_b, vetor_x)

        diferenca_relativa = _calcular_diferenca_relativa_gauss_jacobi(vetor_x, novo_vetor_x)

        vetor_x = novo_vetor_x

    return novo_vetor_x


if __name__ == "__main__":
    m = np.array([[2,1,],[3,4]])

    b = np.array([1,-1])

    x = gauss_jacobi(m,b)

    print(x)
