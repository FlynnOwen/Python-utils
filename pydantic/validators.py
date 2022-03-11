"""
Custom validation and complex relationships between objects can be achieved using the validator decorator
"""
from typing import List
from pydantic import BaseModel, validator, ValidationError


class UserModel(BaseModel):
    name: str
    username: str
    password1: str
    password2: str

    # Validators run on instantiation of the object
    @validator('name')  # Text in the validator == v method argument
    def name_must_contain_space(cls, v):  # Validators are class-methods
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('Passwords do not match')
        return v

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v


user = UserModel(
    name='samuel colvin',
    username='scolvin',
    password1='zxcvbn',
    password2='zxcvbn',
)

# This triggers the name_must_contain_space validator
try:
    UserModel(
        name='samuel',
        username='scolvin',
        password1='zxcvbn',
        password2='zxcvbn2',
    )
except ValidationError as e:
    print(e)

print(user.dict())


class DemoModel(BaseModel):
    square_numbers: List[int] = []
    cube_numbers: List[int] = []

    # '*' represents all attributes
    @validator('*', pre=True)  # pre means evaluate prior to other validators
    def split_str(cls, v):
        if isinstance(v, str):
            return v.split('|')  # can operate on attributes and re-assign them
        return v

    @validator('cube_numbers', 'square_numbers')  # Call validation on multiple attributes
    def check_sum(cls, v):
        if sum(v) > 42:
            raise ValueError('sum of numbers greater than 42')
        return v

    @validator('square_numbers', each_item=True) # each_item calls the validator on each item of an iterable(?)
    def check_squares(cls, v):
        assert v ** 0.5 % 1 == 0, f'{v} is not a square number'
        return v

    @validator('cube_numbers', each_item=True)
    def check_cubes(cls, v):
        # 64 ** (1 / 3) == 3.9999999999999996 (!)
        # this is not a good way of checking cubes
        assert v ** (1 / 3) % 1 == 0, f'{v} is not a cubed number'
        return v


print(DemoModel(square_numbers=[1, 4, 9]))
print(DemoModel(square_numbers='1|4|16'))
print(DemoModel(square_numbers=[16], cube_numbers=[8, 27]))

try:
    DemoModel(square_numbers=[1, 4, 2])
except ValidationError as e:
    print(e)
    """
    1 validation error for DemoModel
    square_numbers -> 2
      2 is not a square number (type=assertion_error)
    """

try:
    DemoModel(cube_numbers=[27, 27])
except ValidationError as e:
    print(e)
