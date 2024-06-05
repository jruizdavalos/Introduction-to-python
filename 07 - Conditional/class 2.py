'''



a= 10

b= 20

if a>5:
    if b>15:
        print("B is Greater than 15 ")
    else:
        print("A is greater than 5, but b is not greater than 15 ")
else:
    print("A is not greater five ")

'''

age = int(input("Enter your age: "))


if age >=18:
    score= int(input("Enter your exam score: "))
    if score>=40:
        print("YOu meet both the age score criteria, you are qualified ")
    else:
        print("Yoy meet th age criteria bur do not meet the score criteria")
else:
    print("YOu do not meet the age criteria, please try when you are above 18")