#Fahrenheit (°F) = (Temperature in degrees celsius (°C) * 9/5)+32.

celsius_temperature = [25,30,15,10,35]

def fahrenheit(c):
    f=32+(c*9/5)
    return f

print(list(map(fahrenheit,celsius_temperature)))

l=list(map(lambda c: c*9/5+32,celsius_temperature))
print("\n ffff: ",l)