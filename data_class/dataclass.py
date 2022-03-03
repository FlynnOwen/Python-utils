from dataclasses import dataclass, field


class Human1:

    def __init__(self, name: str, age: int, gender: str, species: str):
        self.name       =  name
        self.age        =  age
        self.gender     =  gender
        self.species    = species
        self.age_months = self.age * 12

    def say_name(self):
        print('Hi, my name is ' + self.name)


@dataclass
class Human2:
    name   : str
    age    : int
    gender : str
    species: str

    def __post_init__(self):  # Used for attributes that depend on initialised values
        self.age_months = self.age * 12

    def say_name(self):
        print('Hi, my name is ' + self.name)


@dataclass(order=True)  # Define an ordering of data - objects of this class
class Developer(Human2):
    occupation: str
    species: str = field(default='Nerd', init=False)  # Overwrites the inherited value, must use field for default

    def __post_init__(self):
        super().__post_init__()  # Inherit parent __post_init__
        self.sort_index = self.age  # In __post_init__ define the sort index


flynn = Human1('Flynn', 25, 'Male', 'Human')
print(type(flynn))
print(flynn)
print(flynn.name)
print(flynn.age)
print(flynn.gender)
print(flynn.species)
print(flynn.age_months)
flynn.say_name()

flynn = Human2('Flynn', 25, 'Male', 'Human')
print(type(flynn))
print(flynn) # Comes with built-in __repr__ method
print(flynn.name)
print(flynn.age)
print(flynn.gender)
print(flynn.species)
print(flynn.age_months)
flynn.say_name()

flynn = Developer('Flynn', 25, 'Male', 'Developer')
print(type(flynn))
print(flynn) # Comes with built-in __repr__ method
print(flynn.name)
print(flynn.age)
print(flynn.gender)
print(flynn.species)
print(flynn.occupation)
print(flynn.age_months)
flynn.say_name()

katie = Developer('Katie', 26, 'Female', 'Developer')
print(katie > flynn)
