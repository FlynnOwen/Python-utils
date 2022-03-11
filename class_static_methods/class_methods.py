"""
Refers to the class itself, rather than the object instance.
cls used instead of self as the argument.
Generally used to create factory methods - return a class

Usage - polymorphism, constructor methods, factory methods
"""
from dataclasses import dataclass
from datetime import date


@dataclass
class Person:
    name: str
    age: int
    
    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


@dataclass
class Man(Person):
    gender: str = 'Male'


flynn = Person('Flynn', 25)
flynn.display()

# Factory object can be instantiated directly from class
katie = Person.from_birth_year('Katie', 1996)
katie.display()

# Factory object can also be instantiated from an instance
ronan = flynn.from_birth_year('Ronan', 2000)
print(ronan)
ronan.display()

# When a class inherits from a parent class with a class method,
# the child class is instantiated using the child class type
simon = Man.from_birth_year('Simon', 1970)
print(simon)
simon.display()


bindi = simon.from_birth_year('Bindi', 2006)
print(bindi)