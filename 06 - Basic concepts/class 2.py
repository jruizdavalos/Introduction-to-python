'''
a= [1,2,3]
b=[4,5,6]

print(a+b)

c=a+b
print(c)
print(a *3)

a=[1,2,3,4,5,6,7,8]
b=[1,2,[3,4,5],6,7,8,[9,10]]

a[0:4]=[10,20,30]

a[3]=33

print(a)

#tuples

fruits=('apple','orange','mango','pineapple')

print(fruits)

#i can't change tuple object

#Dictonary

people={
    "Jhon":32,
    "Rob":40,
    'Tim':20
}

people_id={1:"Ford",2:"Walton",3:"Paker"}

print(people["Rob"])
people["Rob"]=50

people=dict(
    jhon=32,
    rob=45,
    tim=20

)

print(people)

#add people

people["mike"]=30

print(people)

del people['tim']

print(people)
people={
    "Jhon":32,
    "Rob":40,
    'Tim':20
}
# print(people["jim"]) give message error because it don't found jim


print(people.get("jim"))

prices ={'iphone':500, 'ipad':400}

new_prices={'iphone':600,'imac':1500}

prices.update(new_prices)
print(prices)
a= prices.pop('ipad')
print(prices)

print(a)
'''
prices ={'iphone':500, 'ipad':400, 'imac':1500}

print(prices.values())
print(prices.keys())
print(prices.items())


