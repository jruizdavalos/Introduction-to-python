'''

Write a function which would divide two numbers,
design the function in a manner that it handles the divide by zero exception.
'''

#option 1
def divide():
    a= float(input("Enter nominator number: "))
    b= float(input("Enter Divisor number: "))
    resul=0
    try:
        resul=a/b
    except ZeroDivisionError as e:
        print(f"Error {e}")
    else:
        print(resul)
#option 2

def divide2(a,b):

    try:
        return a/b
    except ZeroDivisionError as e:
        print(f"Error: {e} ")

a=float(input("Enter a number: "))
b= float(input("Enter valu by you want to divide the number: "))

result= divide2(a, b)
print(result)




