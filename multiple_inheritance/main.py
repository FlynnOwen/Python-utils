class Human:
    def __init__(self, age, height, gender):
        self.age = age
        self.height = height
        self.gender = gender

    @property
    def say_age(self):
        return f'My age is {self.age} years old'

    @staticmethod
    def meaning_of_life(number):
        return f'The meaning of life isn\'t {number}... It\'s 42!!'

    @classmethod
    def human_from_meters(cls, age, height_in_meters, gender, *args):
        return cls(age, int(height_in_meters*100), gender, *args)


class Worker:
    def __init__(self, job, salary):
        self.job = job
        self.salary = salary

    def say_salary(self):
        return self.salary

    def get_raise(self):
        self.salary = self.salary * 1.05


class Miner(Human, Worker):
    def __init__(self, age, height, gender, job, salary):
        Human.__init__(self, age, height, gender)
        Worker.__init__(self, job, salary)


class TestClass(Human):
    def __init__(self, age):
        self.attribute = None
        self.age = age


if __name__ == '__main__':
    johnny = Miner(15, 170, 'Male', 'Miner', 75000)
    print(johnny)
    print(johnny.age)
    print(johnny.height)
    print(johnny.gender)
    print(johnny.say_salary())

    doug = Worker('Truck Driver', 50000)
    print(doug.say_salary())

    rodney = TestClass(35)
    print(rodney.say_age)
    print(rodney.meaning_of_life(35))

    tall_sam = Human.human_from_meters(17, 1.9, 'Male')
    print(tall_sam.height)
    print(tall_sam.age)

    tall_rod = Miner.human_from_meters(25, 1.95, 'Male', 'Developer', 25000)
    print(tall_rod.height)
    print(tall_rod.job)
    print(tall_rod.salary)