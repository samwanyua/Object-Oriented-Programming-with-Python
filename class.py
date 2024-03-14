# Classes
class Item:
    # class attributes - belong to class itself
    pay_rate = 0.8 #The pay rate after 20% discount

    # constructor/magic methods
    def __init__(self,name: str,price: float, quantity = 0):
        # print(f"An instance created: {name}")
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to Zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to Zero!"


        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    # methods
    def calculate_total_price(self):

        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    


# instances
item1 = Item("Phone",23,43)
# item1.name = "Phone"
# item1.price = 299
# item1.quantity = 34
print(item1.calculate_total_price())

item2 = Item("Laptop",20,30000)
# item2.name = "Laptop"
# item2.price = 3400
# item2.quantity = 32
print(item2.calculate_total_price())

# print(item2.name)

# methods
# random_string = "aaaddd"
# print(random_string.upper())


# print(item1.name)
# print(item2.name)
# item2.has_numpad = False

print(Item.pay_rate) # accessing class attribute 


# accessing class attribute at instance level
print(item1.pay_rate)

# to see all attributes for class
print(Item.__dict__)

# to see all attributes at instance level
print(item1.__dict__)

item1.apply_discount()
print(item1.price)

# discount for a partilar product
item3 = Item("Macbook", 100000, 1)
item3.pay_rate = 0.7
item3.apply_discount()
print(item3.price)