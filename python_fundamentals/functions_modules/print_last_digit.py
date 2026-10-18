#!/usr/bin/env python3


def print_last_digit(number):
    """Imprime y devuelve el ultimo digito de number (siempre positivo)."""
    if number < 0:
        number = -number
    ultimo = number % 10
    print(ultimo, end="")
    return ultimo
