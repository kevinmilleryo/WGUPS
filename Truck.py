# Create class for trucks
class Truck:
    def __init__(self, capacity, speed, load, packages, mileage, address, departure):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.departure = departure
        self.time = departure
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.load, self.packages, self.mileage,
                                           self.address, self.departure)
