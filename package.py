class Package:
    # Create package object
    def __init__(self, id, address, city, state, zip, deadline, weight, notes, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status

        # Print package objects
        def _str_(self):
            if (self.notes != ""):
                return "{self.id}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.delivery_deadline}, {self.weight}kg, {self.notes}, {self.status}".format(
                    self=self)
            else:
                return "{self.id}, {self.address}, {self.city}, {self.state}, {self.zip}, {self.delivery_deadline}, {self.weight}kg, ..., {self.status}".format(
                    self=self)
