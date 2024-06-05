#Creating a class

class Vehicle:
    #Creating a class attribute
    class_attribute= "This is a vahicle class"

    #Creating a constructor
    def __init__(self,name,color):
        # Instance variables
        self.name= name
        self.color=color

    @classmethod
    def class_method(cls):
        print("This is a class method")
        print(f"I can access the class attribute: {cls.class_attribute}")

    #Instance method
    def display_info(self):
        print(f"Name: {self.name}, Color: {self.color}")

    @staticmethod
    def static_method():
        print("I am a static method, i cannot access anything")
class Car(Vehicle):
    def __init__(self, name,color,fuel_type):
        #self.name=name
        #self.color=color
        #use super function and reduce de variable
        super().__init__(name,color)
        
        self.fuel_type= fuel_type


    def display_info(self):
        print(f"{self.name},{self.color}, {self.fuel_type}")




#Create an object

vehicle= Vehicle("CoolCar","Red")
vehicle.display_info()

car= Car("LuxuryCar","Black","Petrol")
car.display_info()

Vehicle.class_method()
Vehicle.static_method()