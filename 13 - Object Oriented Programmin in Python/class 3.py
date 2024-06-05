'''
def product_data():
    product_name= input("Enter name of the product: ")
    product_price=input("Enter price of the product: ")
    print(product_name)
    print(product_price)

product_data()



'''

class Product:

    def __init__(self,name, price):
        self.name= name
        self.price= price

    def get_data(self):
        self.name=input("Enter name of the product: ")
        self.price= input("Enter price of the product")

    def put_data(self):
        print(self.name)
        print(self.price)

class DigitalProduct(Product):
    def __init__(self,link):
        self.link= link
    def get_link(self):
        self.link=input("Enter product Link")

    def put_link(self):
        print(self.link)


p1= DigitalProduct("")
p1.get_data()
p1.get_link()