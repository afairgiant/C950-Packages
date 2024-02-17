# Student ID:
# Author: Alex Fair

import csv

# Define file path constants
DISTANCE_FILE = "DeliveryData/Distance_table.csv"
ADDRESS_FILE = "DeliveryData/Address_list.csv"
PACKAGE_FILE = "DeliveryData/Package_list.csv"


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


# Define a function to read CSV files
def read_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)


# Read the distance information file
CSV_Distance = read_csv(DISTANCE_FILE)
print(CSV_Distance)
# Read the address information file
CSV_Address = read_csv(ADDRESS_FILE)
print(CSV_Address)
# Read the package information file
CSV_Package = read_csv(PACKAGE_FILE)
print(CSV_Package)


def load_package_data(filename, hash_table):
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)  # Use DictReader to automatically handle the headers
        for row in reader:
            package_id = row["ID"]
            address = row["Address"]
            city = row["City"]
            state = row["State"]
            zipcode = row["Zip"]
            deadline_time = row["Deadline"]
            weight = row["Weight(kg)"]
            status = "At the hub"  # Assuming all packages start at the hub; adjust as necessary
            hash_table.insert(package_id, address, city, state, zipcode, deadline_time, weight, status)
