class Truck:
    def __init__(self, brand, capacity):
        self.brand = brand
        self.capacity = capacity  # capacity in tons
        self.mileage = 0

    def drive(self, distance):
        self.mileage += distance
        return self.mileage

    def load(self, weight):
        if weight <= self.capacity:
            return f'Loaded {weight} tons.'
        else:
            return f'Cannot load {weight} tons. Exceeds capacity of {self.capacity} tons.'

    def __str__(self):
        return f'Truck(brand={self.brand}, capacity={self.capacity} tons, mileage={self.mileage} miles)'
