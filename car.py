class Car:
    def __init__(self, brand):
        self.brand =  brand
        self.mileage = 0

    def drive(self, distance):
        self.mileage += distance
        return self.mileage

    def __str__(self):
        return f'Car(brand={self.brand}, mileage={self.mileage})'
