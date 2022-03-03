from dataclasses import dataclass, field


class Human1:

    def __init__(self, name: str, age: int, gender: str, species: str):
        self.name    =  name
        self.age     =  age
        self.gender  =  gender
        self.species = species

    def say_name(self):
        print('Hi, my name is ' + self.name)


@dataclass
class Human2:
    name   : str
    age    : int
    gender : str
    species: str

    def say_name(self):
        print('Hi, my name is ' + self.name)


@dataclass
class Developer(Human2):
    occupation: str
    species: str = field(default='Nerd', init=False) # Overwrites the inherited value, must use field for default


flynn = Human1('Flynn', 25, 'Male', 'Human')
print(type(flynn))
print(flynn)
print(flynn.name)
print(flynn.age)
print(flynn.gender)
print(flynn.species)
flynn.say_name()

flynn = Human2('Flynn', 25, 'Male', 'Human')
print(type(flynn))
print(flynn) # Comes with built-in __repr__ method
print(flynn.name)
print(flynn.age)
print(flynn.gender)
print(flynn.species)
flynn.say_name()

flynn = Developer('Flynn', 25, 'Male', 'Developer')
print(type(flynn))
print(flynn) # Comes with built-in __repr__ method
print(flynn.name)
print(flynn.age)
print(flynn.gender)
print(flynn.species)
print(flynn.occupation)
flynn.say_name()
