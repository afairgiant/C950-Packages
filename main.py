# Student ID: 001574781
# Author: Alex Fair

import csv

# Define file path constants
DISTANCE_FILE = "DeliveryData/Distance_table.csv"
ADDRESS_FILE = "DeliveryData/Address_list.csv"
PACKAGE_FILE = "DeliveryData/Package_list.csv"


class Package:
    def __init__(
        self, package_id, address, city, state, zipcode, deadline_time, weight, status
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


# Define a function to read CSV files
def read_csv(filename):
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)


# Read the distance information file
CSV_Distance = read_csv(DISTANCE_FILE)
print(f" Distances \n {CSV_Distance} \n")

# Read the address information file
CSV_Address = read_csv(ADDRESS_FILE)
print(f" Address \n {CSV_Address} \n")

# Read the package information file
CSV_Package = read_csv(PACKAGE_FILE)
print(f"Packages \n {CSV_Package} \n")


# Read csv files, and put into hash table
def loadPackageData(HashTable):
    pass
