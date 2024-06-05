'''
def area(radius, pi=3.14):
    result = pi*radius**2
    return result

def cost(circleAre, costPerSqm):
    totalCost = circleAre*costPerSqm
    return totalCost

print(cost(circleAre=area(radius=10,pi=3.15),costPerSqm=2))

def circle(r):
    area= 3.14*r**2
    circumference= 2*3.14*r
    return area, circumference

a,b=circle(r=10)

print(f"area of the circle : {a}-- \n circumference of circle : {b}")

def add(numbers):
    total=0
    for number in numbers:
        total+=number
        print(number)
    return total
score =[1,2,3,4,5]
result= add(score)
print(result)

'''

def removeDuplicate(numbers):
    newList=[]

    for number in numbers:
        if number not in newList:
            newList.append(number)

    return newList

def removeDuplicate2(numbers):
    return list(set(numbers))
ids=[1,2,3,4,5,2,1,7,8,9,1,3,4,10,11,10]

list1= removeDuplicate(ids)

print(list1)

list2 = removeDuplicate2(ids)
print(f"\n\n Otra forma {list2}")
