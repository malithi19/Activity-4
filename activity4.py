from car import Car
from bike import Bike

car1 = Car('Mercedes')
car2 = Car('Toyota')

bike1 = Bike("Yamaha", "Sport")

print(car1)
print(car2)
print(bike1)

# Demonstrate the new methods
car1.drive(100)
car2.drive(200)
bike1.accelerate(50)
bike1.brake(20)

print(car1)
print(car2)
print(bike1)

