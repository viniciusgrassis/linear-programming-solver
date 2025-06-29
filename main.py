import numpy as np
from branch_and_bound.node import Node
from branch_and_bound.validators import tem_float
from branch_and_bound.prepara_BaB import extrai_bases, prepara_restricoes, adiciona_restricoes
from tratamento_entrada.carregar_entrada import carregar_entrada
from tratamento_entrada.criar_tableau import criar_tableau
from metodo_principal.big_m_create import big_m_create
from metodo_principal.big_m_checker import big_m_checker
from metodo_principal.simplex import simplex, linha_pivo, pivoteamento
from metodo_principal.multi_solution_checker import multi_solution_checker
from tratamento_saida.apresentar_solucao import apresentar_solucao

np.set_printoptions(
    suppress=True,      
    precision=2,        
    linewidth=np.inf    
)

def temp():
    c, a, r, b = carregar_entrada("modelo.txt")
    pilha = [Node()] #"arvore" do branch and bound com busca em profundidade
    melhor_tableau = None
    alternativo_melhor = None #só existe se o melhor tiver uma solução alternativa
    if a is not None:
        valido = False
        node = Node()
        pilha.append(node)
        while pilha is not None:
            node = pilha.pop()

            a_extra = prepara_restricoes(node.a, node.coluna_var, a.shape[1])
            novo_a, novo_r, novo_b = adiciona_restricoes(a, r , b, a_extra, node.r, node.b)
            if np.any(novo_r == 0) or np.any(novo_r == 2):
                tableau_inicial = big_m_create(c, novo_a, novo_r, novo_b)
                tableau_final = simplex(tableau_inicial)
                teste = big_m_checker(tableau_final, novo_r, novo_a)

            else:
                tableau_inicial = criar_tableau(c, a, r, b)
                tableau_final = simplex(tableau_inicial)

            base = extrai_bases(tableau_final,  a.shape[1])
            infrator = tem_float(base)
            if infrator is None:
                valido = True 

            teste_coluna = multi_solution_checker(tableau_final)
            if teste_coluna is not None:
                linha_alternativa = linha_pivo(tableau_final, teste_coluna)
                tableau_alternativo = pivoteamento(tableau_final, linha_alternativa, teste_coluna)
                base_alt = extrai_bases(tableau_alternativo, a.shape[1])
                if not valido:
                    infrator = tem_float(base)
                    if infrator is None:
                        valido = True
                    elif valida_entre(tableau_final, tableau_alternativo):
                        valido = True



if __name__ == "__main__":
    c, a, r, b = carregar_entrada("modelo.txt")
    pilha = [] #"arvore" do branch and bound com busca em profundidade
    if a is not None:
        tableau_inicial = None
        if np.any(r == 0) or np.any(r == 2):
            tableau_inicial = big_m_create(c, a, r, b)
            tableau_final = simplex(tableau_inicial)
            teste = big_m_checker(tableau_final, r, a)
            if not teste:
                print("Solução inviável.")
                exit(1)
            else:
                print("Solução viável encontrada.")
                apresentar_solucao(tableau_final, a.shape[1], num_sol=1)
        else:
            tableau_inicial = criar_tableau(c, a, r, b)
            tableau_final = simplex(tableau_inicial)
            apresentar_solucao(tableau_final, a.shape[1], num_sol=1)

        teste_coluna = multi_solution_checker(tableau_final)
        if teste_coluna is not None:
            print("\nMúltiplas soluções:")
            linha_alternativa = linha_pivo(tableau_final, teste_coluna)
            tableau_alternativo = pivoteamento(tableau_final, linha_alternativa, teste_coluna)
            apresentar_solucao(tableau_alternativo, a.shape[1], num_sol=2)
    else:
        print("Erro ao carregar.")
        exit(1)