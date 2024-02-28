# Class representing packages
class Package:
    def __init__(
        self,
        package_id,
        address,
        city,
        state,
        zipcode,
        deadline_time,
        weight,
        status,
        note,
    ):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline_time = deadline_time
        self.weight = weight
        self.status = status  # At hub, loaded, en route, delivered
        self.delivery_time = None  # Only used when delivered.
        self.note = note

    def __str__(self):
        return (
            f"{self.package_id}, "
            f"{self.address}, "
            f"{self.city}, "
            f"{self.state}, "
            f"{self.zipcode}, "
            f"{self.deadline_time}, "
            f"{self.weight}, "
            f"{self.delivery_time}, "
            f"{self.status}"
        )

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
            "Delivery Time": (
                self.delivery_time if self.delivery_time is not None else " "
            ),
        }

    # Create package object that will be inserted into the hash table
