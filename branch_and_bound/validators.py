def tem_float(bases):
    for i, v in enumerate(bases):
        if not (isinstance(v, int) or (isinstance(v, float) and v.is_integer())):
            return i  # Índice da primeira variável fracionária
    return None  # Solução é inteira
