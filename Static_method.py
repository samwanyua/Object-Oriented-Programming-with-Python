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
    
    @staticmethod # you don't access anywhere the class or instance 
    def isWorkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



Employee.set_raise_amount(1.07) # Same as ... Employee.raise_amount = 1.07 

emp_1 = Employee("Sam", "Wanyua", 340000) 
emp_2 = Employee("Dan", "Otieno", 1000)

import datetime
my_date = datetime.date(2024,3,17)
print(Employee.isWorkday(my_date))






