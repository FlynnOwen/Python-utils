"""
A property decorator allows a method to be called as an attribute.
Useful if we have an attribute that depends on other attributes.
"""
from dataclasses import dataclass

"""
naive method: if inflation is changed, inflated_wage doesn't - although it relies on it
"""
@dataclass
class WorkerNaive:
    name: str
    wage: int
    inflation: float = 1.04

    def __post_init__(self):
        self.inflated_wage = self.wage * self.inflation


flynn = WorkerNaive('Flynn', 100000)
print(flynn.name)
print(flynn.wage)
print(flynn.inflation)
print(flynn.inflated_wage) # called as an attribute

flynn.inflation = 1.08
print(flynn.inflated_wage)


"""
Advanced method: using properties / getters / setters
"""
@dataclass
class Worker:
    name: str
    wage: int
    inflation: float = 1.04

    @property
    def inflated_wage(self):
        return self.wage * self.inflation
    

flynn = Worker('Flynn', 100000)
print(flynn.name)
print(flynn.wage)
print(flynn.inflation)
print(flynn.inflated_wage) # called as an attribute

flynn.inflation = 1.08
print(flynn.inflated_wage)