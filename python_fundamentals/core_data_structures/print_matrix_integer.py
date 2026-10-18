#!/usr/bin/env python3


def print_matrix_integer(matrix=[[]]):
    """Imprime una matriz de enteros, una fila por linea."""
    for fila in matrix:
        for i in range(len(fila)):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(fila[i]), end="")
        print()
