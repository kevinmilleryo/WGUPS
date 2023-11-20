# Create class for packages
class Package:
    def __init__(self, ID, address, city, state, zipcode, Deadline_time, weight, status, delivery_truck = "N/A"):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.Deadline_time = Deadline_time
        self.weight = weight
        self.status = status
        self.departure = None
        self.delivery = None
        self.delivery_truck = delivery_truck

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, Truck %s"% (self.ID, self.address, self.city, self.state, self.zipcode,
                                                       self.Deadline_time, self.weight, self.delivery,
                                                       self.status, self.delivery_truck)

    def update_status(self, convert_timedelta):
        if self.delivery < convert_timedelta:
            self.status = "Delivered"
        elif self.departure > convert_timedelta:
            self.status = "En route"
        else:
            self.status = "At Hub"

# class Package():
#
#     # Constructor
#     def __init__(self, id, address, city, state, zip, deadline, weight, note, delivery_status="at the hub", delivery_time="N/A", delivery_truck="N/A", delivery_distance=0):
#         self.id = id
#         self.address = address
#         self.city = city
#         self.state = state
#         self.zip = zip
#         self.deadline = deadline
#         self.weight = weight
#         self.note = note
#         self.delivery_status = delivery_status
#         self.delivery_time = delivery_time
#         self.delivery_truck = delivery_truck
#         self.delivery_distance = delivery_distance
#
#     # Returns a string representation of the package
#     def __str__(self):
#         return f"Package ID: {self.id} Address: {self.address} {self.city}, {self.state} {self.zip} Deadline: {self.deadline} Weight: {self.weight} Note: {self.note} Delivery Status: {self.delivery_status} Delivery Time: {self.delivery_time} Delivery Truck: {self.delivery_truck}"