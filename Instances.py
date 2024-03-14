# Instances and classes
# classes help us to group data and functions in a way it's easy to reuse and easy to build upon
# Method - function associated with a class
# Class is a blueprint for creating instances
# Each uniique  employee we create using Employee class - is an instance of that class
#Instance variable contain data that's unique to each instance



class Employee:
    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'

    def full_name(self):
        return f"{self.first} {self.last}"

        

emp_1 = Employee("Sam", "Wanyua", 340000) #this is an instance of Employee class
print(emp_1.email)

print(emp_1.full_name())
# same as 
print(Employee.full_name(emp_1))




