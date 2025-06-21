import numpy as np
from tratamento_entrada.carregar_entrada import carregar_entrada
from tratamento_entrada.criar_tableau import criar_tableau

def multi_solution_checker(tableau):
    linha_objeto = tableau[0, 1:-1]

    for j in range(len(linha_objeto)):
        indice_coluna = j + 1
        coluna_atual = tableau[:, indice_coluna]

        eh_basica = (np.sum(np.round(coluna_atual, 4)) == 1 and np.count_nonzero(np.round(coluna_atual, 4)) == 1)

        if not eh_basica:
            custo = linha_objeto[j]
            if abs(custo) < 1e-6:
                return indice_coluna
    return None