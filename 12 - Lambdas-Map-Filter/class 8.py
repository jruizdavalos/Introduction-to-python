#Fibonacci

def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        fib_secuence=[0,1]
        fib_secuence.extend(map(lambda i: fib_secuence[i-1]+fib_secuence[i-2],range(2,n)))
        return fib_secuence
fi=fibonacci(10)

print(fi)