# Class represent delivery Trucks


class Truck:
    def __init__(self, capacity, load, mileage, location, speed, depart_time):
        self.capacity = (capacity,)
        self.load = (load,)
        self.mileage = (mileage,)
        self.location = (location,)
        self.speed = (speed,)
        self.depart_time = (depart_time,)

    # def __str__(self):
    #     return "%s, %s, %s, %s, %s, %s" (self.capacity, self.load, self.mileage, self.location, self.speed, self.depart_time)
