#Errors & Exceptions
#Syntax error
#Logical error
#Runtime error
#Exception handling

n= int(input("Enter numerator: "))
d= int(input("Enter dominator: "))
result=0
try:
    resul=n/d

except ZeroDivisionError as e:
    print(f"Cannot divide a number by zero: {e}")
else:
    print(resul)
finally:
    print("This code will be executed no matter what")
