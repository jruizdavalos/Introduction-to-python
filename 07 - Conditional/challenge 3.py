'''
Coding challenge part 3



Task no 1: Using a for-loop and a range function, print "I am a programmer" 5 times.


Task no 2: Create a function which displays out the square values of numbers from 1 to 9.

'''
for x in range(5):
    print(f"I am a programmer : {x}")

def displaySquare():
    for x in range(1,10):
        print(x*x)

displaySquare()
