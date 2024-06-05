
#function lambda
result= (lambda x: x**2)(7)

result1= (lambda x,y: x+y)(2,5)
print(result1)

#funtcion map

numbers=[1,2,3,4,5]


def square(x):
    return x*x

for number in numbers:
    square(number)
    print(square(number))

new_list= list(map(square, numbers))
print(new_list)

