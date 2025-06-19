import numpy as np

def carregar_entrada(entrada):
    lista_c, lista_a, lista_r, lista_b = [], [], [], []

    atual = 'c'

    try:
        with open(entrada, 'r') as f:
            for linha in f:
                linha = linha.strip()

                if not linha:
                    if atual == 'c':
                        atual = 'a'
                    elif atual == 'a':
                        atual = 'r'
                    elif atual == 'r':
                        atual = 'b'
                    continue

                valores = [float(x) for x in linha.split()]
                if atual == 'c':
                    lista_c.extend(valores)
                elif atual == 'a':
                    lista_a.append(valores)
                elif atual == 'r':
                    lista_r.extend(valores)
                elif atual == 'b':
                    lista_b.extend(valores)
            
            c = np.array(lista_c)
            a = np.array(lista_a)
            r = np.array(lista_r)
            b = np.array(lista_b)
            return c, a, r, b

    except FileNotFoundError:
        return None, None, None, None
    except Exception as e:
        return None, None, None, None

if __name__ == "__main__":
    entrada = "modelo.txt"
    c, a, r, b = carregar_entrada(entrada)

