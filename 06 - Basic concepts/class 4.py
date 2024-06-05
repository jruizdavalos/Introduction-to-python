'''


products = ['phone', 'tablet', 'laptop', 'journal']

# displaying products

print(f"Current list of items : {products}")


#

add_items=input("Enter product to add: ")

add_after= input(f"After which product do you want to place {add_items} ")

index = products.index(add_after)
products.insert(index+1, add_items)

print(index)

print(f"Current list of items : {products}")



products = {
    'phone':100,
    'tablet':200,
    'laptop':400,
    'journal':40

}

print(products)

#product= input("Enter product to check the price: ")

#print(f"Price of the {product} is {products[product]}")

new_product = input("Enter a product yoy want to add: ")

new_product_price= input(f"enter price for {new_product}: ")

products[new_product]= new_product_price



'''


products = {
    'phone':100,
    'tablet':200,
    'laptop':400,
    'journal':40

}

print(products)

deleted_products= input("Enter the name of product to be deleted")

del products[deleted_products]

print(f"product deleted,here are update products: {products}")