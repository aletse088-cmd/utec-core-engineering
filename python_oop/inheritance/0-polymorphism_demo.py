#!/usr/bin/env python3
"""Demo of inheritance and polymorphism with animal classes."""


class Animal:
    """Parent class that defines a behavior shared by all animals."""

    def speak(self):
        """Return a generic sound."""
        return "Some sound"


class Dog(Animal):
    """Class that represents a dog and inherits from Animal."""

    def speak(self):
        """Return the sound of a dog (overrides Animal.speak)."""
        return "Woof"


class Cat(Animal):
    """Class that represents a cat and inherits from Animal."""

    def speak(self):
        """Return the sound of a cat (overrides Animal.speak)."""
        return "Meow"


dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())

animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

print(issubclass(Dog, Animal))
