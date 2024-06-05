#decorator 4

def summerDiscountDecorator(func):
    def wrapper(price):
        func(price)
        return func(price/2)
    return  wrapper


@summerDiscountDecorator
def total(price):
    return price

print(total(100))
