# Class represent delivery Trucks


class Truck:
    def __init__(self, capacity, speed, load, mileage, location, departure_time):
        self.capacity = capacity  # Max number of packages
        self.speed = speed  # Constant speed of 18 mph per Task instructions
        self.load = load  # Current packages
        self.mileage = mileage  # Driven miles, increase with each delivery
        self.location = location  # Latest drop off location
        self.departure_time = departure_time  # Time to leave hub

    def __str__(self):
        return f"{self.capacity} - {self.load} - {self.mileage} - {self.location} - {self.speed} - {self.departure_time}"
