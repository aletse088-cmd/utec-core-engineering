#!/usr/bin/env python3


def best_score(a_dictionary):
    """Devuelve la clave con el valor entero mas grande."""
    if not a_dictionary:
        return None
    mejor = None
    for clave in a_dictionary:
        if mejor is None or a_dictionary[clave] > a_dictionary[mejor]:
            mejor = clave
    return mejor
