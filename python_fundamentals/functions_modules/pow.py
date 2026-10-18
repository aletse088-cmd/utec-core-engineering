#!/usr/bin/env python3


def pow(a, b):
    """Devuelve a elevado a la potencia b usando un bucle."""
    negativo = b < 0
    if negativo:
        b = -b
    resultado = 1
    for _ in range(b):
        resultado *= a
    if negativo:
        return 1 / resultado
    return resultado
