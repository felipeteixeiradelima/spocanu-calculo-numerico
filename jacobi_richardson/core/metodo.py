from typing import List

import numpy as np
from numpy import float64
from numpy.linalg import det
from numpy.typing import NDArray

from .exceptions import MatrizInvalidaError, SistemaImpossivelError, SistemaIndeterminadoError

### PARÂMETROS ############################################################

_TOLERANCIA: float = 0.01

### VARIÁVEIS GLOBAIS #####################################################

_ultimo_numero_iteracoes: int

###########################################################################

def _obter_determinantes_incognitas(matriz: NDArray[float64],
                                    vetor_b: NDArray[float64]) -> List[float]:
    
    lista_determinantes: List[float] = []

    n = matriz.shape[0]

    for i in range(n):
        matriz_aux = matriz.copy()
        matriz_aux[:,i] = vetor_b
        determinante = det(matriz_aux)
        lista_determinantes.append(determinante)

    return lista_determinantes

def _checar_sistema(matriz: NDArray[float64],
                    vetor_b: NDArray[float64]):

    d = det(matriz)

    lista_dets_incognitas = _obter_determinantes_incognitas(matriz, vetor_b)

    dets_incognitas_nulas = [d_ic == 0 for d_ic in lista_dets_incognitas]

    if d == 0 and all(dets_incognitas_nulas):
        raise SistemaIndeterminadoError()

    if d == 0:
        raise SistemaImpossivelError()


def _validar_matriz_jacobi_richardson(matriz: List[float] | List[List[float]] | NDArray[float64]) -> None:
    matriz = np.array(matriz)

    n = matriz.shape[0]

    for i in range(n):
        if matriz[i,i] == 0:
            raise MatrizInvalidaError(f"Elemento na posição ({i},{i}) é igual a 0")

def _proxima_iteracao_jacobi_richardson(matriz: List[float] | List[List[float]] | NDArray[float64],
                                   vetor_b: List[float] | List[List[float]] | NDArray[float64],
                                   vetor_x: List[float] | List[List[float]] | NDArray[float64]) -> NDArray[float64]:
    matriz = np.array(matriz)
    vetor_b = np.array(vetor_b)
    vetor_x = np.array(vetor_x)

    _validar_matriz_jacobi_richardson(matriz)

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

def _calcular_diferenca_relativa_jacobi_richardson(vetor_x: List[float] | List[List[float]] | NDArray[float64],
                                                   novo_vetor_x: List[float] | List[List[float]] | NDArray[float64]) -> float:
    vetor_x = np.array(vetor_x)
    novo_vetor_x = np.array(novo_vetor_x)

    dividendo = max(abs(novo_vetor_x - vetor_x))
    divisor = max(abs(vetor_x))

    if divisor == 0:
        return 1

    return dividendo/divisor

def obter_ultimo_numero_iteracoes() -> int:

    return _ultimo_numero_iteracoes

def jacobi_richardson(matriz: List[float] | List[List[float]] | NDArray[float64],
                 vetor_b: List[float] | List[List[float]] | NDArray[float64]) -> NDArray[float64]:

    _checar_sistema(matriz, vetor_b)

    global _ultimo_numero_iteracoes

    _ultimo_numero_iteracoes = 0

    matriz = np.array(matriz)
    vetor_b = np.array(vetor_b)

    n = matriz.shape[0]

    tolerancia = _TOLERANCIA
    diferenca_relativa = 1

    vetor_x = np.zeros(n)

    while diferenca_relativa >= tolerancia:
        novo_vetor_x = _proxima_iteracao_jacobi_richardson(matriz, vetor_b, vetor_x)

        diferenca_relativa = _calcular_diferenca_relativa_jacobi_richardson(vetor_x, novo_vetor_x)

        vetor_x = novo_vetor_x

        _ultimo_numero_iteracoes+=1

    return novo_vetor_x


if __name__ == "__main__":
    m = [[10,2,1],
         [1,5,1],
         [2,3,10]]

    b = [14,11,8]

    x = jacobi_richardson(m,b)

    print(x)
