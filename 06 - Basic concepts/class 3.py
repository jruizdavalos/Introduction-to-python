'''

#numbers = set([1,2,3,4,5,6])
numbers= {1,2,3,4,6,4,5} #set delete duplicate data and keep order

print(numbers)

names ={'jhon','rob','mike','jhon'}
print(names)
s={'jhon',12,4.5,True}
print(type(s))
print(s)

s={}

print(type(s))

#create set empty need use set ()

s= set()

print(type(s))

s ={'Jhon', 'Rob','Matt'}

print('Matt' in s)

seta = {1,2,3,4,5}
setb= {4,5,6,7,8}

s=seta | setb

print(s)
print(seta & setb)

print(seta - setb)
print(setb - seta)

print(setb ^ seta)


seta = {1,2,3,4,5}

seta.add(10)
print(seta)

seta.add(9)
print(seta)

#seta.remove(20) crash
seta.discard(20)
a= seta.pop()

print(seta)

print(a)

seta.clear()

print(seta)


'''


products=['iphone','tablet','laptop','journal']

print(f"current list of item : {products}")


#askinng user to remove a product
remove_item= input("Enter product to remove form the above list : ")

products.remove(remove_item)

print()


#Displying the entire list after romoving item

print(f"current list of item : {products}")


#code to add product


add_item= input("Enter product to Add: ")

products.append(add_item)

print(products)
