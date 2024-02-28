# Student ID: 001574781
# Author: Alex Fair

import csv

from trio import open_file

from hashtable import ChainingHashTable
from package import Package
from truck import Truck

# Define file path constants
DISTANCE_FILE = "DeliveryData/Distance_table.csv"
ADDRESS_FILE = "DeliveryData/Address_list.csv"
PACKAGE_FILE = "DeliveryData/Package_list.csv"


# Define a function to read CSV files
def read_csv(filename):
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)


# Read the distance information file
CSV_Distance = read_csv(DISTANCE_FILE)
# print(f" Distances \n {CSV_Distance} \n")

# Read the address information file
CSV_Address = read_csv(ADDRESS_FILE)
# print(f" Address \n {CSV_Address} \n")

# Read the package information file
CSV_Package = read_csv(PACKAGE_FILE)
# print(f"Packages \n {Package_Data} \n")

# Initiate hash table
PackageHashTable = ChainingHashTable()


# Read package csv file, and put into hash table
def loadPackageData(packageFile):
    with open(packageFile) as packageList:
        packageData = csv.reader(packageList, delimiter=",")
        next(packageData)  # skip header
        for package in packageData:
            package_id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zipcode = package[4]
            deadline_time = package[5]
            weight = package[6]  # in KG
            status = "At Hub"
            note = package[7]

            # Package Object
            package_object = Package(
                package_id,
                address,
                city,
                state,
                zipcode,
                deadline_time,
                weight,
                status,
                note,
            )
            print(f"package {package_object}")
            # Add each package to hash table
            PackageHashTable.insert(package_id, package_object)


loadPackageData(PACKAGE_FILE)
print(PackageHashTable.print_table())
