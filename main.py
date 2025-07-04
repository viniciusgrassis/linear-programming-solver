import numpy as np
from branch_and_bound.node import Node
from branch_and_bound.prepara_BnB import extrai_bases, prepara_restricoes, adiciona_restricoes, tem_float
from metodo_principal.solucionador import resolver_problema
from tratamento_entrada.carregar_entrada import carregar_entrada
from tratamento_saida.apresentar_solucao import apresentar_solucao

np.set_printoptions(
    suppress=True,      
    precision=2,        
    linewidth=np.inf    
)

if __name__ == "__main__":
    c, a, r, b = carregar_entrada("modelo.txt")
    pilha = [Node()] # "arvore" do branch and bound com busca em profundidade
    melhor_tableau = [None, None]

    if a is not None:
        valido = False
        while len(pilha) != 0:
            print(f"tamanho da pilha: {len(pilha)}")
            node = pilha.pop()
            
            if node.coluna_var is not None:
                a_extra = prepara_restricoes(node.coluna_var, a.shape[1])
                novo_a, novo_r, novo_b = adiciona_restricoes(a, r, b, a_extra, node.r, node.b)
            else:
                novo_a, novo_r, novo_b = a, r, b

            tableaus = resolver_problema(c, novo_a, novo_r, novo_b)
            num_sol = len(tableaus) if tableaus is not None else 0

            if num_sol == 0:
                continue

            base = extrai_bases(tableaus[0], a.shape[1])
            invalido = tem_float(base)

            if num_sol == 2:
                base_alt = extrai_bases(tableaus[1], a.shape[1])
                invalido_alt = tem_float(base_alt)

            if invalido == None:
                z = -tableaus[0][0, -1]
                if melhor_tableau[0] is None or z > -melhor_tableau[0][0, -1]:
                    melhor_tableau[0] = tableaus[0]
                    if(num_sol == 2):
                        melhor_tableau[1] = tableaus[1]
                    else:
                        melhor_tableau[1] = None

            if num_sol == 2 and invalido_alt is None:
                z_alt = -tableaus[1][0, -1]
                if melhor_tableau[0] is None or z_alt > -melhor_tableau[0][0, -1]:
                    melhor_tableau[0] = tableaus[1]
                    melhor_tableau[1] = tableaus[0]
                continue
            if melhor_tableau[0] is not None and z < -melhor_tableau[0][0, -1]:
                continue
            if invalido is not None:
                menor = int(base[invalido])
                maior = int(base[invalido] + 1)
                pilha.append(Node(invalido, 2, maior))
                pilha.append(Node(invalido, 1, menor))

        if melhor_tableau[0] is None:
            print("Solução inviavel.")
            exit(1)
        else:
            apresentar_solucao(melhor_tableau[0], a.shape[1], num_sol=1)
            if melhor_tableau[1] is not None:
                apresentar_solucao(melhor_tableau[1], a.shape[1], num_sol=2)
        