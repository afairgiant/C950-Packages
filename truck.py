# Class represent delivery Trucks

class Truck:
    def __init__(self, load, maxLoad, speed, currentLocation, hub, ):
        self.hub = hub
        self.speed = speed
        self.load = load
        self.maxLoad = maxLoad
        self.currentLocation = currentLocation
