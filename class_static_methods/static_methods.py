"""
Static methods are generally used to group functionality of functions within a class.
"""
from dataclasses import dataclass, field


@dataclass
class Human:
    name: str
    age: int
    job: str = field(default="Developer")

    @staticmethod
    def do_work():  # A static method doesn't require self as an argument
        print('Doing work')

    def say_name(self):
        print(f"My name is {self.name}")


flynn = Human('Flynn', 25)
flynn.do_work()
flynn.say_name()

Human.do_work()  # We can call a static method without instantiating an object first
try:
    Human.say_name()
except TypeError:
    print("You need to instantiate a class to use a non-static method!")

