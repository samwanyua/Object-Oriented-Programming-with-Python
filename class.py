# Classes
class Item:
    # methods
    def calculate_total_price(self,x,y):
        return x * y

# instances
item1 = Item()
item1.name = "Phone"
item1.price = 299
item1.quantity = 34
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = "Laptop"
item2.price = 3400
item2.quantity = 32
print(item2.calculate_total_price(item2.price, item2.quantity))

print(item2.name)

# methods
random_string = "aaaddd"
print(random_string.upper())

