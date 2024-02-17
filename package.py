# Class representing packages
class Package:
    def __init__(self, package_id, address, city, state, zipcode, deadline_time, weight, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline_time = deadline_time
        self.weight = weight
        self.status = status  # At hub, loaded, en route, delivered
        self.delivery_time = None  # Only used when delivered.

    def status_update(self):
        pass
    # Will need to update status throughout

    def lookup_package_info(self):
        return {
            "Delivery Address": self.address,
            "Delivery Deadline": self.deadline_time,
            "Delivery City": self.city,
            "Delivery Zip Code": self.zipcode,
            "Package Weight": self.weight,
            "Delivery Status": self.status,
            "Delivery Time": self.delivery_time if self.delivery_time is not None else " "
        }
