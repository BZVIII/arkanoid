def creaPersona(**argumentos):
    d = {}
    for clave, valor in argumentos.items():
        if isinstance(valor, str):
            d[clave] = valor.upper()
        elif isinstance(valor, int):
            d[clave] = float(valor)
        else:
            d[clave] = valor

    return d
    
        