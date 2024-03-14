# regular methods, class methods and static methods

'''
* Regular methods in a class take instance as the first argument(self)
* Class methods - take a class as the first argument
* Static method - don't pass anything automatically - neither class or instance



'''
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


Employee.set_raise_amount(1.07) # Same as ... Employee.raise_amount = 1.07 

emp_1 = Employee("Sam", "Wanyua", 340000) 
emp_2 = Employee("Dan", "Otieno", 1000)

#  Class method constructors
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Kim-John-43500'
emp_str_3 = 'Alecs-Chei-50000'

first, last, pay = emp_str_1.split('-')
new_emp_1 = Employee(first,last, pay)

print(new_emp_1.email)

emp_10 = Employee.from_string(emp_str_2)
print(emp_10.email)


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

