#decorated
'''


def chocolate():
    print("Chocolate")

def decorator(func):
    def wrapper():
        print("Wrapper up side")
        func()
        print("Wrapper down side")
    return wrapper
chocolate= decorator(chocolate)
chocolate()


#decorate 2
def decorator(func):
    def wrapper():
        print("Wrapper up side")
        func()
        print("Wrapper down side")
    return wrapper


@decorator
def chocolate():
    print("Chocolate")

@decorator
def cake():
    print("cake")

chocolate()
cake()

'''

#decoraor 3

#decorate 2
def decorator(func):
    def wrapper(*args,**Kwargs):
        print("Wrapper up side")
        func(*args,**Kwargs)
        print("Wrapper down side")
    return wrapper


@decorator
def chocolate():
    print("Chocolate")

@decorator
def cake(name):
    print("cake "+ name)

chocolate()
cake("coco")


