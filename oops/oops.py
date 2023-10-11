class Employee:
    
    # constructor
    def __init__(self, first, last, pay):
        
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    

emp_1 = Employee('Mohd', 'Arshad', 50000)
emp_2 = Employee('Test', 'User', 80000)

# calling method from instance therefore no need to pass instance
emp_1.fullname()

# calling method from class therefore we pass the instance value 
Employee.fullname(emp_1)