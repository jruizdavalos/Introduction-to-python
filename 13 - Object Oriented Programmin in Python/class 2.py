class Product:
    quantity= 400
    def __init__(self, name, price):
        self.name=name
        self.price=price

    def summer_discount(self, discount):
        self.price= self.price*(1-discount/100)


p1= Product("Tshirt",10)
print(p1.name)
print(p1.price)

p1.summer_discount(20)

print("\n price with discount: ",p1.price)


