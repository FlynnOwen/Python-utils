from dataclasses import dataclass


class Human1:

    def __init__(self, name: str, age: int, gender: str):
        self.name   = name
        self.age    = age
        self.gender = gender

    def say_name(self):
        print('Hi, my name is ' + self.name)


@dataclass
class Human2:
    name  : str
    age   : int
    gender: str

    def say_name(self):
        print('Hi, my name is ' + self.name)


flynn = Human1('Flynn', 25, 'Male')
print(type(flynn))
print(flynn)
print(flynn.name)
print(flynn.age)
print(flynn.gender)
flynn.say_name()

flynn = Human2('Flynn', 25, 'Male')
print(type(flynn))
print(flynn) # Comes with built-in __repr__ method
print(flynn.name)
print(flynn.age)
print(flynn.gender)
flynn.say_name()