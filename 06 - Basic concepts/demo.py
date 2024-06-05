'''
print('Hola mundo')

a=5
b=3

print(a**b)

a = int(input("Enter first number "))
b= int(input("Enter second number "))
print(type(a))
c= a + b
print(c)

class 33
firstName= input("Enter first Name: ")
lastName= input("Enter second Name: ")

userName= firstName+lastName
print(userName)
email= userName+"@gmail.com"

print(email)


class 37
#SI = P * N * R /100

principal = int(input("Enter the amount borrowed: "))
years = float(input("Enter the period in years "))
rate = float(input("Enter rate of interest "))

interest = principal * years * rate /100

print("Simple interest on the principal amount : "+str(interest))

class 38
#BMI = weight in gks / (height in m)^2

weight = float(input("Enter weight in KGS : " ))
height = float(input("Enter hieght in meters: "))
bmi = weight/(height*height)

print(f"BMI is : {bmi}")


people= ['Jhon', 'Rob','Mike','Rose']

print(people)


fruits = ['apple','mango','peach','orange','watermelon','grape']

print('apple' in fruits)

print('apple' not in fruits)

'''

fruits = ['apple','mango','peach','orange','watermelon','grape']

fruits.append('lemon')
fruits.insert(1,"Pineapple")
fruits.extend(['guava','apricot'])
print(len(fruits))

print(fruits)

fruits.remove('apricot')
print(fruits)

fruits.pop() #remove last element
print(fruits)

print(fruits.index('orange'))

score=[1,2,3,4,5,6,7,90,30]

print(max(score))
print(min(score))