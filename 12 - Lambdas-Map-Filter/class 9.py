numbers= [2,3,4,5,6,7,8,9,10]

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

print(is_prime(59))

filters=list(filter(is_prime,numbers))

print(filters)