import numpy as np
from carregar_entrada import carregar_entrada
from criar_tableau import criar_tableau
from big_m_create import big_m_create
from simplex import simplex

if __name__ == "__main__":
    c, a, r, b = carregar_entrada("modelo.txt")
    if a is not None:
        tableau_inicial = None
        if np.any(r != 1) or np.any(r != 2):
            tableau_inicial = big_m_create(c, a, r, b)
            print("Tableau inicial com Big M:")
            print(tableau_inicial)
            tableau_final = simplex(tableau_inicial)
            print("Tableau final:")
            print(tableau_final)
        else:
            tableau_inicial = criar_tableau(c, a, r, b)
            print("Tableau inicial:")
            print(tableau_inicial)
            tableau_final = simplex(tableau_inicial)
            print("Tableau final:")
            print(tableau_final)
    else:
        print("Erro ao carregar.")
        exit(1)