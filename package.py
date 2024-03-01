# Class representing packages
from datetime import timedelta


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
            truck,
            loadTime
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
        self.truck = None # Only used when loaded
        self.loadTime = None

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

    def status_update(self, current_datetime):
        loadTime = self.loadTime
        #print(self.delivery_time)
        #print(self.loadTime)
        #print(current_datetime)
        # Update package status
        if current_datetime < loadTime:
            self.status = "At Hub"
        elif current_datetime == loadTime:
            self.status = "Loaded on " + self.truck
        elif loadTime < current_datetime < self.delivery_time:
            self.status = "En Route on " + self.truck
        elif current_datetime > self.delivery_time:
            self.status = "Delivered"
        else:
            self.status = "Contact Support"

    def packageLookup(self):
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
    def reportDeliveryTime(self, current_datetime):
        if self.delivery_time < current_datetime:
            # print("Package has been delivered")
            report_DeliveryTime = f"Delivery Time: {self.delivery_time}"

        else:
            # print("Package has not been delivered")
            # If package hasn't been delivered show estimated time
            report_DeliveryTime = f"Estimated Delivery Time: {self.delivery_time}"

        return report_DeliveryTime
    def packageReport(self, reportType, current_datetime):
        # Report package status
        reportDelivery = self.reportDeliveryTime(current_datetime)
        self.status_update(current_datetime)

        if reportType == "status":
            return (
                f"\033[4mPackage Report for package #{self.package_id}\033[0m\n"
                f"Package ID: {self.package_id}\n"
                f"Delivery Deadline: {self.deadline_time}\n"
                f"Delivery Address: {self.address}\n"
                f"Delivery City: {self.city}\n"
                f"Delivery Zip Code: {self.zipcode}\n"
                f"Package Weight: {self.weight}\n"
                f"Delivery Status: {self.status}\n"
                f"{reportDelivery}"
            )
        elif reportType == "time":
            return (
                f"Package ID: {self.package_id} Delivery Status: {self.status}. {reportDelivery}"
            )
        else:
            pass
