#Factorial

def factorial(num):
    if num ==1:
        return 1
    elif num==0:
        return 0
    else:
        return num * factorial(num-1)

print(factorial(5))

#arguments
def add(*args):
    sum=0
    for n in args:
        print(n)
        sum+=n
    return sum

#

def product(**Kwargs):
    for key,value in Kwargs.items():
        print(key+":"+value)





product(name="Iphone",price="200")


product(name="ipad",price="500", description="This is an ipad")

