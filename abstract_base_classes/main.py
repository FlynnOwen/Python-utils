# import abstract base class module
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def age_in_months(self):
        return self.age * 12


class AbstractChildClassNoAbstractMethod(AbstractClass):
    def exclaim_name(self):
        return self.name + '!'


class AbstractChildClass(AbstractClass):
    def age_in_months(self):
        return self.age * 12


if __name__ == '__main__':
    # Instance of parent abstract class
    try:
        error_object = AbstractClass('Rod', 35)
    except TypeError:
        print('You can\'t just instantiate an abstract class like that you fool!!')

    # Instance of child class that doesn't have abstract method
    try:
        error_object_2 = AbstractChildClassNoAbstractMethod('Rod', 35)
    except TypeError:
        print('You need to include all abstract methods from the abstract parent class!!')

    # Instance of child class
    error_child_object = AbstractChildClass('Rod', 35)
    print(error_child_object.age)
    print(error_child_object.name)
    print(error_child_object.age_in_months())