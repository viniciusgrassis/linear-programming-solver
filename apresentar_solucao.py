import numpy as np

def apresentar_solucao(tableau_final, num_var, num_sol = 1):
    try:
        solucao_str = ""
        if num_sol > 1:
            solucao_str += f"\n---/ Solução ótima alternativa {num_sol - 1} /---"
        else:
            solucao_str += "\n---/ Solução ótima encontrada /---"

        z_otimo = tableau_final[0, -1]*-1
        solucao_str += f"\nValor ótimo para Z = {z_otimo:.2f}"
        solucao_str += "\n\n---/ Variáveis básicas /---\n"

        for i in range(num_var):
            coluna_x = tableau_final[:, i + 1]
            valor = 0.0

            if np.sum(np.round(coluna_x, 4)) == 1 and np.count_nonzero(np.round(coluna_x, 4)) == 1:
                linha_base = np.where(np.round(coluna_x, 4) == 1)[0][0]
                valor = tableau_final[linha_base, -1]

            solucao_str += f"\n x{i + 1} = {valor:.2f}"

        print(solucao_str)
        return True

    except Exception as e:
        print(f"Erro ao apresentar a solução: {e}")
        return False
