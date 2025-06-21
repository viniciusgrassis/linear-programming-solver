import numpy as np
from carregar_entrada import carregar_entrada
from criar_tableau import criar_tableau
from big_m_create import big_m_create
from big_m_checker import big_m_checker
from simplex import simplex, linha_pivo, pivoteamento
from multi_solution_checker import multi_solution_checker

np.set_printoptions(
    suppress=True,      
    precision=2,        
    linewidth=np.inf    
)

if __name__ == "__main__":
    c, a, r, b = carregar_entrada("modelo.txt")
    if a is not None:
        tableau_inicial = None
        if np.any(r == 0) or np.any(r == 2):
            tableau_inicial = big_m_create(c, a, r, b)
            print("Tableau inicial com Big M:")
            print(tableau_inicial)
            tableau_final = simplex(tableau_inicial)
            teste = big_m_checker(tableau_final, r, a)
            if not teste:
                print("Solução inviável.")
                exit(1)
            else:
                print("Solução viável encontrada.")
                print("Tableau final:")
                print(tableau_final)
        else:
            tableau_inicial = criar_tableau(c, a, r, b)
            print("Tableau inicial:")
            print(tableau_inicial)
            tableau_final = simplex(tableau_inicial)
            print("Tableau final:")
            print(tableau_final)

        teste_coluna = multi_solution_checker(tableau_final)
        if teste_coluna is not None:
            print("Múltiplas soluções:")
            linha_alternativa = linha_pivo(tableau_final, teste_coluna)
            tableau_alternativo = pivoteamento(tableau_final, linha_alternativa, teste_coluna)
            print("Tableau alternativo:")
            print(tableau_alternativo)
    else:
        print("Erro ao carregar.")
        exit(1)