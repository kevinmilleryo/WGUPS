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



# class Truck():
#
#     # Constructor
#     def __init__(self, id, capacity, packages, float_time=0, distance=0, current_address="4001 South 700 East", current_city="Salt Lake City", current_state="UT", current_zip="84107"):
#         self.id = id
#         self.capacity = capacity
#         self.packages = packages
#         self.float_time = float_time
#         self.distance = distance
#         self.current_address = current_address
#         self.current_city = current_city
#         self.current_state = current_state
#         self.current_zip = current_zip
#
#     # Returns a string representation of the truck
#     def __str__(self):
#         return f"Truck ID: {self.id} Capacity: {self.capacity} Packages: {self.packages}"