class Product:

    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    def display(self):
        print(f"This is {self.id}")
        print(f"This is {self.name}")
        print(f"This is {self.quantity}")
        print(f"This is {self.price}")

    def bill(self):
        return self.quantity * self.price


p = Product(2021, "Dairy milk", 3, 10)
print(p)
p.display()
p.bill()
