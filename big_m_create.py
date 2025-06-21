import numpy as np
from carregar_entrada import carregar_entrada
from criar_tableau import criar_tableau

def big_m_create(c, a, r, b):
    tableau = criar_tableau(c, a, r, b)

    M = np.max(np.abs(tableau))*100

    colunas_artificiais = []

    num_variaveis = a.shape[1]
    coluna_folga = num_variaveis + 1

    num_excesso = np.sum(r != 2)
    coluna_art = num_variaveis + num_excesso + 1

    for i in range(len(r)):
        if r[i] == 0:
            colunas_artificiais.append(coluna_art)
            coluna_art += 1
            coluna_folga += 1
        elif r[i] == 2:
            colunas_artificiais.append(coluna_art)
            coluna_art += 1
        else:
            coluna_folga += 1

    for coluna in colunas_artificiais:
        tableau[0, coluna] = -M

        linha_artificial = np.where(tableau[:, coluna] == 1)[0][0] + 1

        tableau[0, :] = tableau[0, :] + tableau[linha_artificial, :]*M

    return tableau