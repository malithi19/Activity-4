class Bike:
	def __init__ (self, name, bike_type):
		self.name = name
		self.type = bike_type
		self.speed = 0
		
	def accelerate(self, increment):
        	self.speed += increment
        	return self.speed

    	def brake(self, decrement):
        	self.speed -= decrement
        	if self.speed < 0:
            		self.speed = 0
        	return self.speed

    	def __str__(self):
        	return f'Bike(name={self.name}, type={self.type}, speed={self.speed})'
	
