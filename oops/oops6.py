# property decorator basically helps in accessing methods like attributes
class Employee:
    
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Cena')
emp_1.fullname = 'Mohd Arshad'
emp_1.first = 'Jim'


print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)




    