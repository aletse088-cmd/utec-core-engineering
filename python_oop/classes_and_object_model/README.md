# Classes and Object Model

This directory contains exercises about creating classes and working with
objects in Python.

## Tasks

### 1. My first square
`0-square.py` defines an empty class `Square` that represents a square.

### 2. Square with a private size
`1-square.py` defines a class `Square` with a private instance attribute
`size`, set when the object is created.

### 3. Square with validated size
`2-square.py` defines a class `Square` whose private `size` must be an
integer (`TypeError` otherwise) and greater than or equal to 0 (`ValueError`
otherwise).

### 4. Area of a square
`3-square.py` adds the instance method `area(self)` to `Square`, which
returns the area of the square.

### 5. Access and update a private attribute
`4-square.py` adds a getter and a setter (with validation) for the private
attribute `size` of `Square`, using the `property` decorator.

### 6. Print a square
`5-square.py` adds the public instance method `my_print(self)` to `Square`,
which prints the square with the character `#` (an empty line if size is 0).
