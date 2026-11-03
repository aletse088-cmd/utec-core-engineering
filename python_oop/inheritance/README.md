# Inheritance

This directory contains exercises about inheritance and polymorphism in
Python.

## Tasks

### 0. Introduction to inheritance and polymorphism
`0-polymorphism_demo.py` defines a parent class `Animal` and the subclasses
`Dog` and `Cat`, overrides `speak()` in each subclass, demonstrates
polymorphism with a list of animals, and checks class relationships with
`isinstance` and `issubclass`.

### 1. Basic geometry
`base_geometry.py` defines a class `BaseGeometry` with an `area()` method
that raises an exception (not implemented) and an `integer_validator()`
method that checks a value is an integer greater than 0.

### 2. Rectangle
`1-rectangle.py` defines a class `Rectangle` that inherits from
`BaseGeometry`, with private `width` and `height` validated by the inherited
`integer_validator()`.

### 3. Full rectangle
`2-rectangle.py` extends `Rectangle` with an implementation of `area()` and
a `__str__` method that returns `[Rectangle] <width>/<height>`.

### 4. Square #1
`1-square.py` defines a class `Square` that inherits from `Rectangle`. It
takes a single private `size`, validated by `integer_validator()`, and
implements `area()`.
