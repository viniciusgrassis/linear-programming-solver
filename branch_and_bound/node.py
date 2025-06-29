class Node:
    def __init__(self, coluna_var = None, a_extra = None, r_extra = None, b_extra = None):
        # essa é apenas a restrição extra, o restante é calculado com os dados originais salvos na main
        self.coluna_var = coluna_var
        self.a = a_extra
        self.r = r_extra
        self.b = b_extra