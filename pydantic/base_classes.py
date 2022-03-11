from typing import List
from pydantic import BaseModel


class Human1:
    def __init__(self, id: int):
        self.id = id
        self.name = 'Bob'


class Human2(BaseModel):
    id: int
    name = 'Bob'


katie = Human1(1)
flynn = Human2(id=2)

# Cool things you can do with Basemodel objects
print(flynn.dict())
print(flynn.json())
print(flynn.schema())


# Hierarchical models
class Foo(BaseModel):
    count: int
    size: float = None


class Bar(BaseModel):
    apple = 'x'
    banana = 'y'


class Spam(BaseModel):
    foo: Foo
    bars: List[Bar]


m = Spam(foo={'count': 4}, bars=[{'apple': 'x1'}, {'apple': 'x2'}])
print(m)
print(m.dict())
print(m.json())
