class Employee:
    raise_amount = 1.04 

    def __init__(self, first,last):
        self.first = first
        self.last = last
        # self.email = first + "." + last + '@company.com'

    @property # we're able to access 'email' like an attribute i.e emp_1.email .. instead of emp_1.email()
    def email(self):
        return f"{self.first}.{self.last}@email.com"
    
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    
    # setter
    @full_name.setter
    def full_name(self,name): #name is the value we're trying to set
        first,last = name.split(' ')
        self.first = first
        self.last = last

    # delete fullname
    @full_name.deleter
    def full_name(self): #name is the value we're trying to set
        print("Delete Name!")
        self.first = None
        self.last = None
    

    

    
emp_1 = Employee('John', 'Smith')

emp_1.first = "Jontesdf"

# Ensure you have a setter first!
emp_1.full_name = "Wanyua Samuel" 


# print(emp_1.full_name())
print(emp_1.full_name) # after adding the property decorator
# print(emp_1.email())
print(emp_1.email)

# deleting full name
del emp_1.full_name