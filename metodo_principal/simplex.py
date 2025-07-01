import numpy as np
from tratamento_entrada.carregar_entrada import carregar_entrada
from tratamento_entrada.criar_tableau import criar_tableau

def coluna_pivo(linha_obj):
    valores = linha_obj[1:-1]
    maior = np.max(valores)

    if maior > 0:
        coluna_pivo = np.argmax(valores) + 1
        return coluna_pivo
    else:
        return -1

def linha_pivo(tableau, coluna_pivo):
    valores = tableau[1:, coluna_pivo]
    b = tableau[1:, -1]

    if np.all(valores <= 0):
        return None
    
    razoes = np.divide(b, valores, out=np.full_like(b, np.inf), where=valores > 0)

    linha_pivo = np.argmin(razoes) + 1

    if razoes[linha_pivo - 1] != np.inf:
        return linha_pivo
    else:
        return None

def pivoteamento(tableau, linha_pivo, coluna_pivo):
    num_linhas = tableau.shape[0]
    pivo = tableau[linha_pivo, coluna_pivo]

    fatores = tableau[:, coluna_pivo].copy()

    tableau[linha_pivo, :] = tableau[linha_pivo, :] / pivo

    for i in range(num_linhas):
        if i != linha_pivo:
            fator = fatores[i]
            tableau[i, :] = tableau[i, :] - fator * tableau[linha_pivo, :]
    
    return tableau

def simplex(tableau_inicial):
    tableau = tableau_inicial.copy()
    num_iteracoes = 1

    while True:

        linha_obj = tableau[0]
        indice_coluna_pivo = coluna_pivo(linha_obj)

        if indice_coluna_pivo == -1: #solução ótima
            break       

        indice_linha_pivo = linha_pivo(tableau, indice_coluna_pivo)
        
        if indice_linha_pivo is None:
            print("Solucoes ilimitadas.")
            break
                 
        tableau = pivoteamento(tableau, indice_linha_pivo, indice_coluna_pivo)
        num_iteracoes += 1

    return tableau   