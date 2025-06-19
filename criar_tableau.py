import numpy as np
from carregar_entrada import carregar_entrada

def criar_tableau(c, a, r, b):
    num_res, num_var = a.shape

    num_folga = np.sum(r != 2)
    num_artificiais = np.sum(r != 1) 

    num_colunas = num_var + num_folga + num_artificiais + 2

    tableau = np.zeros((num_res + 1, num_colunas))

    tableau[0, 0] = 1  
    tableau[0, 1:num_var + 1] = c

    col_folga = num_var + 1
    col_artificial = num_var + num_folga + 1

    for i in range(num_res):

        tableau[i + 1, 1:num_var + 1] = a[i]
        tableau[i + 1, -1] = b[i]

        if r[i] == 1:
            tableau[i + 1, col_folga] = 1
            col_folga += 1

        elif r[i] == 0:
            tableau[i + 1, col_folga] = -1
            col_folga += 1

            tableau[i + 1, col_artificial] = 1
            col_artificial += 1

        elif r[i] == 2:
            tableau[i + 1, col_artificial] = 1
            col_artificial += 1

    return tableau
