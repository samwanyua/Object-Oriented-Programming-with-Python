# Classes
class Item:
    # constructor/magic methods
    def __init__(self,name: str,price: float, quantity = 0):
        # print(f"An instance created: {name}")
        # Run validation to the received arguments
        assert price >= 0, f"{price} is not greater than or equal to Zero!"
        assert quantity >= 0, f"{quantity} is not greater than or equal to Zero!"


        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity




    # methods
    def calculate_total_price(self):

        return self.price * self.quantity
    


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
item2.has_numpad = False
