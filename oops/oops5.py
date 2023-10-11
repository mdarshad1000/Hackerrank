class Employee:
    
    raise_amount = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first}.{self.last}@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # repr is used as a fallback for str if str isn't defined
    def __repr__(self) -> str:
        return f"Employee('{self.first}', '{self.last}', {self.pay})"
        
    def __str__(self) -> str:
        return f'{self.fullname()} - {self.email}'
    
    # to add the salary of two employees
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
    

emp_1 = Employee('Mohd', 'Arshad', 90000)
emp_2 = Employee('Test', 'User', 80000)

# __str__ has precedence over __repr__
# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))

# int and str objects have dunder add methods (__add__)
# print(int.__add__(1,2))
# print(str.__add__('1', '2'))
# print('test'.__len__())

# using the dunder method
print(emp_1 + emp_2)
print(len(emp_1))
    