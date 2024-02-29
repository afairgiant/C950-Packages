# Class represent delivery Trucks


class Truck:
    def __init__(self, Id, capacity, speed, load, mileage, location, departure_time):
        self.Id = Id  # Truck ID number
        self.capacity = capacity  # Max number of packages
        self.speed = speed  # Constant speed of 18 mph per Task instructions
        self.load = load  # Current packages
        self.mileage = mileage  # Driven miles, increase with each delivery
        self.location = location  # Latest drop off location
        self.departure_time = departure_time  # Time to leave hub
        self.time = departure_time  # Tracking time of delivery starting from departure time

    def __str__(self):
        return f"Truck#{self.Id} - {self.capacity} - {self.load} - {self.mileage} - {self.location} - {self.speed} - {self.departure_time}"
