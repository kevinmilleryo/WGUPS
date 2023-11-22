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

    # Create class for packages
    def update_status(self, convert_timedelta):
        if self.delivery < convert_timedelta:
            self.status = "Delivered"
        elif self.departure > convert_timedelta:
            self.status = "En route"
        else:
            self.status = "At Hub"
