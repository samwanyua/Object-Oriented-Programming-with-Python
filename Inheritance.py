class Employee:
    raise_amount = 1.04 

    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'


    def full_name(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# Inheritance(subclass)
class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first,last,pay,prog_lang):
        super().__init__(first, last, pay) # same as.... Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def remove_employee(self, emp):
        if emp  in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        for emp in self.employees:
            print(emp.full_name() + ".")
        




dev1 = Developer("Sam", "Wanyua", 340000, "Java") 
dev2 = Developer("Dan", "Otieno", 100000, "C++")


manager1 = Manager('Sue', 'Smith', 90000, [dev1])
print(manager1.email)

manager1.print_employees()
# add employees
manager1.add_employee(dev2)
manager1.print_employees()
# remove employees
manager1.remove_employee(dev2)
manager1.print_employees()

print(isinstance(manager1,Manager)) # tells us if an object is an instance of a class
print(isinstance(manager1,Employee))


print(issubclass(Manager,Employee)) # tells us if a class is a subclass of another

# print(dev1.email)
# print(dev2.email)
# print(help(Developer))

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)

# print(dev1.email)
# print(dev2.prog_lang)



