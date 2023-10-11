class Employee:

    # class variable
    raise_amount = 1.04
    num_of_employee = 0
    
    # constructor
    def __init__(self, first, last, pay):
        
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # not using self to call num_of_employee(class var) because it would not make sense to change/call it for any instance
        Employee.num_of_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        # using self to call raise_amount(class var) because it might be needed to change it for each instance
        self.pay = int(self.pay * self.raise_amount)

    # class method is used to make modification for the entire class
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    # class methods as alternative constructors
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # functions which just have logical connection to the class (!if we do not access class or instance!)
    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    
emp_1 = Employee('Mohd', 'Arshad', 50000)
emp_2 = Employee('Test', 'User', 80000)

# If we want to initialize an employee in the form of a string
emp3_str = 'John-Wick-15000'

# here the emp_3 is initialized using the classmethod from_string
emp_3 = Employee.from_string(emp3_str)

# class method is called using the class, it is usually/generally not called via instance
Employee.set_raise_amount(1.08)

print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_3.fullname())
print(emp_3.email)
print(emp_3.pay)

import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_work_day(my_date))