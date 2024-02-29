# Student ID: 001574781
# Author: Alex Fair

import csv
import datetime
from tkinter import FALSE, TRUE

from hashtable import ChainingHashTable
from package import Package
from truck import Truck

# Define file path constants
DISTANCE_FILE = "DeliveryData/Distance_table.csv"
ADDRESS_FILE = "DeliveryData/Address_list.csv"
PACKAGE_FILE = "DeliveryData/Package_list.csv"

Debug = FALSE


# Define a function to read CSV files
def read_csv(filename):
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)


# Read the distance information file
CSV_Distance = read_csv(DISTANCE_FILE)
if Debug:
    print(f" Distances \n {CSV_Distance} \n")

# Read the address information file
CSV_Address = read_csv(ADDRESS_FILE)
if Debug:
    print(f" Address \n {CSV_Address} \n")

# Read the package information file
CSV_Package = read_csv(PACKAGE_FILE)
if Debug:
    print(f"Packages \n {CSV_Package} \n")

# Initiate hash table
PackageHashTable = ChainingHashTable()


# Read package csv file, and put into hash table
def loadPackageData(packageFile, hashtable):
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
            # Debug print each package enter
            if Debug:
                print(f"    DEBUG: package {package_object}")
            print(f"Inserting package: {package_object.package_id}")
            # Add each package to hash table
            hashtable.insert(package_id, package_object)


# Truck Info
TruckSpeed = 18
TruckCapacity = 16
Truck1_Load = [2, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20]
Truck2_Load = [1, 3, 6, 18, 35, 36, 37, 38, 39, 40]
Truck3_Load = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
Truck1_Departure = datetime.timedelta(hours=8)
Truck2_Departure = datetime.timedelta(hours=10)
Truck3_Departure = datetime.timedelta(hours=10)

# Create Trucks
truck1 = Truck(TruckCapacity, TruckSpeed, Truck1_Load, 0.0, 1, Truck1_Departure)
# print(f"Truck #1 {truck1}")
truck2 = Truck(TruckCapacity, TruckSpeed, Truck2_Load, 0.0, 1, Truck2_Departure)
# print(f"Truck #2 {truck2}")
truck3 = Truck(TruckCapacity, TruckSpeed, Truck3_Load, 0.0, 1, Truck3_Departure)


# print(f"Truck #3 {truck3}")

# Function to convert CSV data into a 2D list
def loadDistanceData(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Determine the number of points
    header = lines[0].strip().split(',')
    num_points = len(header) - 1  # Exclude the ID column

    # Initialize a 2D list with zeros
    distance_matrix = [[0.0 for _ in range(num_points)] for _ in range(num_points)]

    # Process each line (excluding the header) to fill the 2D list
    for line in lines[1:]:  # Skip header
        row = line.strip().split(',')
        point_id = int(row[0]) - 1  # Adjust for 0-indexing

        for i in range(1, len(row)):
            if row[i]:  # If there's a distance value
                distance = float(row[i])
                distance_matrix[point_id][i - 1] = distance
                distance_matrix[i - 1][point_id] = distance  # Mirror the distance for bi-directionality

    return distance_matrix


def loadAddressData(file_path):
    addressData = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            headers = file.readline().strip().split(',')
            for line in file:
                values = line.strip().split(',')
                row_data = {header: value for header, value in zip(headers, values)}
                addressData.append(row_data)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []  # Return an empty list or handle the error as appropriate

    return addressData

try:
    distanceData = loadDistanceData(DISTANCE_FILE)
    print(distanceData)
except Exception as e:
    print(f"AN error occurred: {e}")

try:
    addressData = loadAddressData(ADDRESS_FILE)
    print(addressData)
except Exception as e:
    print(f"An error occurred: {e}")


# Method that will sort the packages in each truck using nearest neighbor
def optimising_delivery(truck):
    # Pull packages from each truck as unsorted array

    unsorted_packages = []
    # Pulls packages set for said truck and puts them into an array for the algorithm.
    for package_id in truck.load:
        package = package.PackageHashTable.search(package_id)
        unsorted_packages.append(package)
    truck.load.clear()  # Empties truck after they've been loaded into unsorted_packages array, so it can be filled
    print("Trucks cleared")  # after sorting.

    # Algorithm to sort the packages
    # Find package closest to the hub and start from there
    # Then find the nearest one from there. Give an error of total miles is > 140
    if Debug:
        print("Sorting Packages")


class Main:
    print("Western Governors University Parcel Service (WGUPS)")
    print("Loading Package Data \n")

    # Load CSV_Package into hash table
    loadPackageData(PACKAGE_FILE, PackageHashTable)

    # print(PackageHashTable.print_table())
