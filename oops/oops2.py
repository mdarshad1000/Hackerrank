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

emp_1 = Employee('Mohd', 'Arshad', 50000)
emp_2 = Employee('Test', 'User', 80000)

# changing class variable from class changes it's value for all instance
Employee.raise_amount = 1.07

# chaging class variable from instance changes the class var only for that instance
emp_1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_employee)