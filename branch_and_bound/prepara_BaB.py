import numpy as np

def extrai_bases(tableau, num_var):
    solucao = []
    for i in range(num_var):
        coluna_x = tableau[:, i + 1]
        valor = 0.0

        if np.sum(np.round(coluna_x, 4)) == 1 and np.count_nonzero(np.round(coluna_x, 4)) == 1:
            linha_base = np.where(np.round(coluna_x, 4) == 1)[0][0]
            valor = tableau[linha_base, -1]
        solucao.append(valor)
    return solucao

def prepara_restricoes(valor_a = None, coluna_var = None, num_var = None):
    if valor_a is not None:
        linha = np.zeros(num_var)
        linha[coluna_var] = valor_a
        return linha
    else: 
        return None

def adiciona_restricoes(a, r, b, a_extra = None, r_extra = None, b_extra = None):
    if a_extra is not None:
        novo_a = np.append(a, [a_extra], axis=0)
        novo_r = np.append(r, r_extra)
        novo_b = np.append(b, b_extra)
    else:
        novo_a, novo_r, novo_b = a, r, b

    return novo_a, novo_r, novo_b




