class Human:
    def __init__(self, age, height, gender):
        self.age = age
        self.height = height
        self.gender = gender

    def say_age(self):
        return f'My age is {self.age} years old'


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


if __name__ == '__main__':
    johnny = Miner(15, 170, 'Male', 'Miner', 75000)
    print(johnny)
    print(johnny.age)
    print(johnny.height)
    print(johnny.gender)
    print(johnny.say_salary())

    doug = Worker('Truck Driver', 50000)
    print(doug.say_salary())
