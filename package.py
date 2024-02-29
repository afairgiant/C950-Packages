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
        destination_index,
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
        self.destination_index = int(destination_index)


    def __str__(self):
        return (
            f"{self.package_id}, "
            f"{self.address}, "
            f"{self.city}, "
            f"{self.state}, "
            f"{self.zipcode}, "
            f"{self.deadline_time}, "
            f"Weight:{self.weight}, "
            f"{self.delivery_time}, "
            f"Status: {self.status}, "
            f"Dest Index: {self.destination_index}"
        )

    def status_update(self):
        pass

    # Will need to update status throughout

    def lookup_package_info(self):
        return (
            f"Package ID: {self.package_id}\n"
            f"Delivery Address: {self.address}\n"
            f"Delivery Deadline: {self.deadline_time}\n"
            f"Delivery City: {self.city}\n"
            f"Delivery Zip Code: {self.zipcode}\n"
            f"Package Weight: {self.weight}\n"
            f"Delivery Status: {self.status}\n"
            f"Delivery Time: {self.delivery_time if self.delivery_time is not None else ' '}\n"
            )