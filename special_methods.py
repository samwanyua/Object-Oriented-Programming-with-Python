# special methods/ magic/dunder methods
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

    @classmethod # class method - class (cls) as the first argument
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first,last, pay = emp_str.split('-')
        return cls(first,last,pay) # create new employee
    
    def __repr__(self):
        return f"Employee ('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.full_name()} - {self.email}"
    
    # combine salary
    def __add__(self, other):
        return self.pay + other.pay
    
    # length of fullname
    def __len__(self):
        return len(self.full_name())


Employee.set_raise_amount(1.07) # Same as ... Employee.raise_amount = 1.07 

emp_1 = Employee("Sam", "Wanyua", 340000) 
emp_2 = Employee("Dan", "Otieno", 100000)

# print(emp_1)
# print(repr(emp_2))
# print(str(emp_2))

# same as
print(emp_1.__repr__())
print(emp_1.__str__())


# more dunder methods
print(int.__add__(34,45))

print(str.__add__('John','Paul'))

# calculating total pay
print(emp_1 + emp_2)

# length of employee full name
print(len('test'))
print('test'.__len__())
print(len(emp_1))

