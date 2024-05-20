from car import Car
from bike import Bike
from truck import Truck

car1 = Car('Mercedes')
car2 = Car('Toyota')
bike1 = Bike("Yamaha", "Sport")
truck1 = Truck('Volvo', 15)  # 15 tons capacity

# Demonstrate the new methods
car1.drive(100)
car2.drive(200)
bike1.accelerate(50)
bike1.brake(20)
truck1.drive(300)
print(truck1.load(10))  
print(truck1.load(20))  

print(car1)
print(car2)
print(bike1)
print(truck1)


