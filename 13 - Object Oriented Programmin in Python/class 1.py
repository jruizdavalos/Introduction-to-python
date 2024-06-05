class Product:
    quantity=200

    def __init__(self, name, price):
        self.name=name
        self.price= price

p1= Product('Phone','22')
print(p1.name)
print(p1.price)

p2 = Product("laptop","900")

print(p2.name)
print(p2.price)
