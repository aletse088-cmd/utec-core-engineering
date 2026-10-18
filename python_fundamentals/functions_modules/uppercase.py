#!/usr/bin/env python3


def uppercase(str):
    """Imprime str en mayúsculas usando ord() y chr()."""
    resultado = ""
    for c in str:
        codigo = ord(c)
        if 97 <= codigo <= 122:
            codigo -= 32
        resultado += chr(codigo)
    print("{}".format(resultado))
