'''

cart = []
n= int(input("ENter the number of items you want to add to the cart "))


for x in range(n):
    item=input("Enter an item into the cart: ")
    cart.append(item)
    print(cart)

print(cart)

'''

cart= []

while True:
    choice= input("Do you want to add item to the cart ? ")
    if choice =='yes':
        item = input("Enter the item you want to add:_ ")
        cart.append(item)
        print(f"Current cart contents are {cart}")
    else:
        break

print(cart)



