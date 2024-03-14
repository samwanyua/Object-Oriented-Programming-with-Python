# class variables shared among all instances in a class
# Instance variables are unique for each instance

class Employee:
    raise_amount = 1.04 # this is a class variable
    all = [] 

    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'

        Employee.all.append(self)

    def full_name(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return  f"Employee('{self.first}', '{self.last}', '{self.pay}')"


    

emp_1 = Employee("Sam", "Wanyua", 340000) #this is an instance of Employee class
print(emp_1.email)
print(Employee.full_name(emp_1))
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

emp_2 = Employee("Dan", "Otieno", 1000)

print(emp_1.__dict__) 
# print(Employee.__dict__) 
print(Employee.all)

for instance in Employee.all:
    print(instance.email)

emp_2.raise_amount = 1.06
emp_2.apply_raise()
print(emp_2.raise_amount)
print(emp_2.pay)