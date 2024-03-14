class Item:
    pay_rate = 0.8 # class attribute
    all = [] 

    def __init__(self,name: str,price: float, quantity = 0):
        # validations
        assert price >= 0, f"Price {price} is not greater than or equal to Zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to Zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute - appending instances to 'all' list
        Item.all.append(self)




    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # __repr__ magic method - rep your objects
    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"
        
        

# instances
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item1 = Item("Mouse", 50, 5)
item1 = Item("Keyboard", 75, 5)

# all items
print(Item.all)

# all names
for instance in Item.all:
    print(instance.name)

# CSV - Comma separated values (allow data to be saved in table structured format )
    
