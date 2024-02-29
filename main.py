# Student ID: 001574781
# Author: Alex Fair

import csv
import datetime

from hashtable import ChainingHashTable
from package import Package
from truck import Truck

# Define file path constants
DISTANCE_FILE = "DeliveryData/Distance_table.csv"
ADDRESS_FILE = "DeliveryData/Address_list.csv"
PACKAGE_FILE = "DeliveryData/Package_list.csv"

Debug = False


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
    """
    Load package data from a file and insert it into the hashtable.

    Args:
    packageFile (str): The file containing package data.
    hashtable (HashTable): The hashtable to insert the package data into.
    """

    # Create a map of address to id
    address_id_map = {address_data['Address']: address_data['Id'] for address_data in addressData}

    # Open the package file and read the data
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

            # Get the destination index from the address_id_map
            destination_index = int(99999999)
            destination_index = address_id_map.get(address, destination_index)

            # Create a Package object
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
                destination_index
            )
            # Debug print each package enter
            if Debug:
                print(f"    DEBUG: package {package_object}")
            #print(f"Inserting package: {package_object.package_id}")
            # Add each package to hash table
            hashtable.insert(package_id, package_object)


# Truck Info
TruckSpeed = 18
TruckCapacity = 16
Truck1_Load = [2, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20]
Truck2_Load = [1, 3, 6, 18, 35, 36, 37, 38, 39, 40]
Truck3_Load = [9, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
Truck1_Departure = datetime.timedelta(hours=8)
Truck2_Departure = datetime.timedelta(hours=10)
Truck3_Departure = datetime.timedelta(hours=12)

# Create Trucks
truck1 = Truck(1, TruckCapacity, TruckSpeed, Truck1_Load, 0.0, 1, Truck1_Departure)
# print(f"Truck #1 {truck1}")
truck2 = Truck(2, TruckCapacity, TruckSpeed, Truck2_Load, 0.0, 1, Truck2_Departure)
# print(f"Truck #2 {truck2}")
truck3 = Truck(3, TruckCapacity, TruckSpeed, Truck3_Load, 0.0, 1, Truck3_Departure)
# print(f"Truck #3 {truck3}")


def loadDistanceData(file_path):
    """
    Load distance data from a file and create a distance matrix.

    Args:
        file_path (str): The path to the file containing distance data.

    Returns:
        list: A 2D list representing the distance matrix.
    """
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
    """
    Load address data from the specified file path and return it as a list of dictionaries.

    Parameters:
    file_path (str): The path to the file containing the address data.

    Returns:
    list: A list of dictionaries representing the address data.
    """
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


def distanceBetween(index1, index2, distance_data):
    """
    Calculate the distance between two locations based on their indices in the distance_data array.

    Args:
    index1 (int): The index of the first location.
    index2 (int): The index of the second location.
    distance_data (list): A 2D list representing the distances between locations.

    Returns:
    float or str: The distance between the two locations, or an error message if the indices are out of bounds.
    """
    try:
        return float(distance_data[index1][index2])
    except IndexError:
        print(f"     ERROR:One or both of the provided indices are out of bounds.\n"
              f"    {index1} & {index2}")
        raise IndexError("One or both of the provided indices are out of bounds.")
    except Exception as e:
        print(f"    ERROR: An error occurred: {str(e)}")
        raise e
def optimized_delivery(truck, distance_data):
    """
    Optimize the delivery route for the given truck using the distance data.

    Args:
    truck: Truck object representing the delivery truck
    distance_data: Dictionary containing distance data between locations

    Returns:
    None
    """
    # Print truck start message
    print(f"Starting Truck#{truck.Id}")

    # Convert truck load to package objects
    unsorted_packages = [PackageHashTable.search(package_id) for package_id in truck.load]
    truck.load.clear()  # Clear the truck's load for re-loading sorted packages
    for package in unsorted_packages:
        package.status = "En Route"  # Update package status to "En Route"
    while unsorted_packages:
        # Find the next closest package to the current truck location
        closest_package, closest_distance = find_closest_package(truck.location, unsorted_packages, distance_data)

        # Update truck and package status based on delivery
        deliver_package(truck, closest_package, closest_distance)

        # Remove the delivered package from unsorted list
        unsorted_packages.remove(closest_package)
    if Debug:
    # Print truck end message with mileage
        print(f"Truck# {truck.Id} - Mileage: {truck.mileage}")


def find_closest_package(current_location, packages, distance_data):
    """
    Find the closest package to the current location.

    Args:
    current_location (int): The current location index.
    packages (list): List of package objects.
    distance_data (dict): Dictionary containing distance data.

    Returns:
    tuple: The closest package and the distance to it.
    """
    closest_package = None  # Initialize the closest package
    closest_distance = float('inf')  # Initialize with infinity

    for package in packages:
        distance = distanceBetween(current_location, package.destination_index, distance_data)
        if distance < closest_distance:
            closest_package, closest_distance = package, distance

    return closest_package, closest_distance


def deliver_package(truck, package, distance):
    """
    Delivers a package using a truck and updates relevant information.

    Args:
    truck (Truck): The truck used for delivery
    package (Package): The package to be delivered
    distance (float): The distance to be traveled for delivery
    """
    # Add distance to truck's mileage
    truck.mileage += distance

    # Update truck's location to package's destination
    truck.location = package.destination_index

    # Calculate and update delivery time
    delivery_time = calculate_delivery_time(distance, truck.speed)
    truck.time += delivery_time

    # Update package status and delivery time
    package.delivery_time = truck.time
    package.status = "Delivered"

    # Print delivered package information
    if Debug:
        print(f"Delivered Package {package.packageLookup()}")

def calculate_delivery_time(distance, speed):
    """Calculate delivery time given distance and speed, returning a timedelta object."""
    return datetime.timedelta(hours=distance / speed)



# Method that will sort the packages in each truck using nearest  algorithm
# def optimized_delivery(truck):
#     print(f"Starting Truck#{truck.Id}")
#     # Pull packages from each truck as unsorted array
#     print(f"Truck Load: {truck.load}")
#     unsorted_packages = []
#     # Pulls packages set for said truck and puts them into an array for the algorithm.
#     for package_id in truck.load:
#         # print(package_id)
#         package = PackageHashTable.search(package_id)
#         print(f"{package} \n")
#         unsorted_packages.append(package)
#
#     truck.load.clear()  # Empties truck after they've been loaded into unsorted_packages array, so it can be filled
#     print("Trucks unsorted load cleared")  # after sorting.
#
#     # Algorithm to sort the packages
#     # Find package closest to the hub and start from there
#     # Then find the nearest one from there. Give an error of total miles is > 140
#     if Debug:
#         print("Sorting Packages")
#     while len(unsorted_packages) > 0:
#         closest_package = unsorted_packages[0]
#         next_address = int(0)
#         if Debug:
#             print("Closest Package: " + str(closest_package.lookup_package_info()))
#         for package in unsorted_packages:
#             if Debug:
#                 print("Package: " + str(package))
#             if distanceBetween(truck.location, package.destination_index, distanceData) < distanceBetween(truck.location, closest_package.destination_index, distanceData):
#                 next_address = distanceBetween(package.destination_index, closest_package.destination_index, distanceData)
#                 print(next_address)
#                 closest_package = package
#         truck.load.append(closest_package.package_id)  # Loads closest package onto truck
#         unsorted_packages.remove(closest_package)  # Removes closest package from unsorted array after delivery
#         truck.mileage += next_address  # Adds distance between the closest package and current location
#         truck.location = closest_package.destination_index  # Changes current location to the closest package location after delivery
#         truck.time += datetime.timedelta(hours=next_address/truck.speed)  # Adds time to delivery
#         closest_package.delivery_time = truck.time  # Sets delivery time of current package
#         closest_package.status = "Delivered"  # Sets status to delivered
#         print(f"Package {closest_package.lookup_package_info()} \n")
#     print(f"Truck# {truck.Id} - Milage: {truck.mileage}")

class Main:
    # Load CSV_Package into hash table
    loadPackageData(PACKAGE_FILE, PackageHashTable)
    optimized_delivery(truck1, distanceData)
    optimized_delivery(truck2, distanceData)
    Truck3_Departure = min(truck1.time, truck2.time)  # Keep truck 3 at Hub until truck or Truck 1 Finish
    # print(Truck3_Departure)
    optimized_delivery(truck3, distanceData)

    print("\nWestern Governors University Parcel Service (WGUPS)")
    print("Loading Package Data")

    print(f"Total Mileage: {truck1.mileage + truck2.mileage + truck3.mileage}")
    print(f"Truck 1 Mileage: {truck1.mileage}")
    print(f"Truck 2 Mileage: {truck2.mileage}")
    print(f"Truck 3 Mileage: {truck3.mileage}")

    # loop until user is satisfied
    isExit = True
    while isExit:
        print("\nPackage Lookup\n")

        print("1. Package Lookup by ID")
        print("2. Package Lookup by Time")
        print("3. Exit Program")
        user_input = input("Enter 1, 2, or 3: ")
        if user_input == "1":
            print("Please Enter a time for the lookup. In format HH:MM:SS \n example: 12:00:00")
            time_input = input()
            hours, minutes, seconds = map(int, time_input.split(':'))
            time_delta = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
            print(time_delta)
            print("Enter Package ID Number")
            package_id = int(input())
            package = PackageHashTable.search(package_id)
            if package:
                package.status_update(time_delta)
                print(package.packageLookup())
                input("Press Enter to Continue...")
            else:
                print("Package Not Found")
        if user_input == "2":
            timeLookup(PackageHashTable)
        if user_input == "3":
            isExit = False