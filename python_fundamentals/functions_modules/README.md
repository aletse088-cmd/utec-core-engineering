# Python - Funciones y modularidad

Proyecto sobre definicion de funciones, valores de retorno, ejecucion de
scripts e importacion de modulos.

## Archivos

| Archivo | Descripcion |
|---------|-------------|
| `islower.py` | Devuelve True si un caracter es letra minuscula (ASCII) |
| `uppercase.py` | Imprime una cadena en mayusculas con `ord()` y `chr()` |
| `print_last_digit.py` | Imprime y devuelve el ultimo digito de un numero |
| `pow.py` | Calcula a elevado a b con un bucle, sin `**` |
| `simple_add.py` | Funcion `add` protegida con `if __name__ == "__main__"` |
| `test_import.py` | Importa `simple_add` para observar el comportamiento |
| `add_0.py` | Define la funcion `add(a, b)` |
| `add.py` | Importa `add` desde `add_0` e imprime `1 + 2 = 3` |

## Requisitos

- Ubuntu 20.04 LTS, Python 3.8.x
- Estilo PEP8 (pycodestyle 2.7.x)
- Primera linea: `#!/usr/bin/env python3`
