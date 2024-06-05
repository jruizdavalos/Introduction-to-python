'''
def hello():
    print("hello world")
    print("hi")
    print("Tom")

hello()

def add(a,b):
    print(a+b)

a= int(input("Enter number one: "))
b=int(input("Enter Number two: "))
add(a,b)


def speed(distance,time):
    print(distance/time)

speed(time=2,distance=100)# use keyword in arguments


#default parameter

def area( radius,pi=3.14):
    print(pi*radius**2)

area(10)

'''

def cost(circleArea, costPerSqm):
    result=(circleArea*costPerSqm)
    return result

r= cost(circleArea=35,costPerSqm=100)

print(r)
