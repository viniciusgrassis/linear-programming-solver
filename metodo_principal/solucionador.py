import numpy as np
from tratamento_entrada.criar_tableau import criar_tableau
from metodo_principal.big_m_create import big_m_create
from metodo_principal.big_m_checker import big_m_checker
from metodo_principal.simplex import simplex, linha_pivo, pivoteamento
from metodo_principal.multi_solution_checker import multi_solution_checker

def resolver_problema(c, a, r, b):
    if a is None:
        print("a vazio.")
        return None

    tableaus_finais = []
    
    if np.any(r == 0) or np.any(r == 2):
        tableau_inicial = big_m_create(c, a, r, b)
        tableau_final = simplex(tableau_inicial)
        if not big_m_checker(tableau_final, r, a):
            return None
        else:
            tableaus_finais.append(tableau_final)
    else:
        tableau_inicial = criar_tableau(c, a, r, b)
        tableau_final = simplex(tableau_inicial)
        tableaus_finais.append(tableau_final)

    # Verifica se há múltiplas soluções
    teste_coluna = multi_solution_checker(tableau_final)
    if teste_coluna is not None:
        linha_alt = linha_pivo(tableau_final, teste_coluna)
        tableau_alternativo = pivoteamento(tableau_final, linha_alt, teste_coluna)
        tableaus_finais.append(tableau_alternativo)

    return tableaus_finais