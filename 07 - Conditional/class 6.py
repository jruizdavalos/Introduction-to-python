products =[
    {'name':"smartphone","price":500,"description":"A handheld device"},
    {'name':'tablet', "price":1000,"description":"A portable computer them"},
    {'name':'Headpohones', "price":50,"description":"A pair of earphone"},
    {'name':'smartwatch', "price":300,"description":"A wearable device used for fitness tracking and received "},
    {'name':'Bluetooth', "price":100,"description":"A portable speaker that connects wirelessly to devices "}
    ]

cart =[]

while True:
    choice= input("Do you want to continue shopping ? ")
    if choice=='yes':
        print("Here is a list of products an their prices")
        for index,product in enumerate(products):
            print(f"\t {index}:{product['name']} \n\t\t {product['description']} \n\t\t {product['price']}\n")



        product_id=int(input("Enter the id of the product you want to add the cart"))

        #Check if product is already present in the cart
        if products[product_id] in cart:
            products[product_id]['quantity']+=1
        else:
            products[product_id]['quantity'] = 1
            cart.append(products[product_id])


        total=0
        print(f"Current cart contents are {cart}")
        for product in cart:
            print(f"{product['name']}: {product['price']}: QTY:{product['quantity']}")
            total= total + product['price']*product['quantity']
        print(f"Cart total is: ${total}")

    else:
        break

print(f"Thank you, you final cart contents are {cart}")



