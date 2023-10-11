class Employee:

    raise_amount = 1.04
    num_of_employee = 0
    
    def __init__(self, first, last, pay):
        
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    

class Developer(Employee):
    
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang): 
        super().__init__(first, last, pay) 
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())



dev_1 = Developer('Mohd', 'Arshad', 80000, 'Python')
dev_2 = Developer('Test', 'User', 70000, 'Java')

# print(dev_1.fullname())
# print(dev_1.prog_lang)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# print(mgr_1.email)

# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()

# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Developer))
# print(isinstance(mgr_1, Employee))

print(issubclass(Developer, Manager))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Employee, Manager))



