'''
Custom exceptions can be defined by inheriting from the Exception class in the Python base library
'''

MAX_SALARY = 1000000
MIN_SALARY = 0


class ValueTooSmallError(Exception):
    """ Raised when a value is too small """
    pass


class ValueTooHighError(Exception):
    """ Raised when a value is too high """
    pass


class Employee:

    def __init__(self,
                 name: str,
                 department: str,
                 salary: int):
        self.name = name
        self.department = department

        if salary < MIN_SALARY:
            raise ValueTooSmallError("Employee must have a positive salary")
        elif salary > MAX_SALARY:
            raise ValueTooHighError("Employee is paid way too much!!!")
        self.salary = salary

    def __repr__(self):
        return self.name


class Payroll:

    def __init__(self, company: str):
        self.company = company
        self.employees = []

    def register_employee(self, employee: Employee):
        """ Adds an employee to payroll """
        self.employees.append(employee)

    def give_pay_rise(self, amount):
        """ Gives a raise by amount to all registered employees """
        for employee in self.employees:
            if employee.salary + amount > MAX_SALARY:
                raise ValueTooHighError("Employee is paid way too much!!!")
            employee.salary += amount


if __name__ == '__main__':
    payroll = Payroll('Google')
    
    flynn = Employee('Flynn', 'IT', 500)
    doug = Employee('Doug', 'Sales', 500)
    
    payroll.register_employee(flynn)
    payroll.register_employee(doug)

    payroll.give_pay_rise(100)

    print(payroll.employees)

    try:
        samwise = Employee('Samwise', 'CEO', 10000000)
    except ValueTooHighError as e:
        print(e)

    try:
        samdumb = Employee('Samdumb', 'Volunteer', -500)
    except ValueTooSmallError as e:
        print(e)