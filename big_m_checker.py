import numpy as np
from carregar_entrada import carregar_entrada
from criar_tableau import criar_tableau
from big_m_create import big_m_create

def big_m_checker(tableau_final, r, a):
    colunas_artificiais = []

    num_variaveis = a.shape[1]
    coluna_folga = num_variaveis + 1

    num_excesso = np.sum(r != 2)
    coluna_art = num_variaveis + num_excesso + 1   

    for i in range(len(r)):
        if r[i] == 0 or r[i] == 2:
            colunas_artificiais.append(coluna_art)
            coluna_art += 1

    for coluna in colunas_artificiais:
        if np.sum(tableau_final[:, coluna]) == 1 and np.count_nonzero(tableau_final[:, coluna]) == 1:
            linha_artificial = np.where(tableau_final[:, coluna] == 1)[0][0]
            valor = tableau_final[linha_artificial, -1]

            if valor > 1e-6:
                return False

    return True


