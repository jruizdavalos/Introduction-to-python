class Student:
    # Class variable
    category="student"



    def __init__(self,name):
        #instance variable
        self.name=name

    #Instance method
    def hello(self):
        print(f"Hello my nami is {self.name}")

    #Instance method
    def name_length(self):
        return len(self.name)


    @classmethod
    def info(cls):
        print(f"This is a method of the class: {cls.category}")

    @staticmethod
    def add(a,b):
        print(a+b)


student1= Student("Jhon")
print(Student.info())
student1.hello()
length= student1.name_length()
print(length)

Student.info()
Student.add(4,5)

class Circle:

    @staticmethod
    def area(r):
        return 3.14*r**2
    @staticmethod
    def cicumference(r):
        return 2*3.14*r


a= Circle.area(10)
print(a)
c= Circle.cicumference(10)
print(c)



