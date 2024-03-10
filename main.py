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

# Set debug mode for print statements
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
PackageHashTable = ChainingHashTable(40)


# Read package csv file, and put into hash table
def loadPackageData(packageFile, hashtable):
    """
    Load package data from a file and insert it into the hashtable.

    Args:
    packageFile (str): The file containing package data.
    hashtable (HashTable): The hashtable to insert the package data into.
    """

    # Create a map of address to id
    address_id_map = {
        address_data["Address"]: address_data["Id"] for address_data in addressData
    }

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
            truck = None  # Set to empty string
            loadTime = None  # Set to empty string

            # Get the destination index from the address_id_map
            destination_index = int(99999999)  # Initialize to a large number
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
                destination_index,
                truck,
                loadTime,
            )
            # Debug print each package enter
            if Debug:
                print(f"    DEBUG: package {package_object}")
            # Add each package to hash table
            hashtable.insert(package_id, package_object)


# Truck Info
TruckSpeed = 18  # Constant Speed per task parameters
TruckCapacity = 16  # Constant max capacity per task parameters
Truck1_Load = [2, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20]
Truck2_Load = [1, 3, 6, 18, 25, 29, 35, 36, 37, 38, 39, 40]
Truck3_Load = [9, 21, 22, 23, 24, 26, 27, 28, 30, 31, 32, 33, 34]
Truck1_Departure = datetime.timedelta(hours=8)
Truck2_Departure = datetime.timedelta(hours=9, minutes=6)
Truck3_Departure = datetime.timedelta(hours=10, minutes=30)

# Create Trucks
truck1 = Truck(1, TruckCapacity, TruckSpeed, Truck1_Load, 0.0, 0, Truck1_Departure)
if Debug:
    print(f"Truck #1 {truck1}")
truck2 = Truck(2, TruckCapacity, TruckSpeed, Truck2_Load, 0.0, 0, Truck2_Departure)
if Debug:
    print(f"Truck #2 {truck2}")
truck3 = Truck(3, TruckCapacity, TruckSpeed, Truck3_Load, 0.0, 0, Truck3_Departure)
if Debug:
    print(f"Truck #3 {truck3}")


def loadDistanceData(file_path):
    """
    Load distance data from a file and create a distance matrix.

    Args:
        file_path (str): The path to the file containing distance data.

    Returns:
        list: A 2D list representing the distance matrix.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Determine the number of points
    header = lines[0].strip().split(",")
    num_points = len(header) - 1  # Exclude the ID column

    # Initialize a 2D list with zeros
    distance_matrix = [[0.0 for _ in range(num_points)] for _ in range(num_points)]

    # Process each line (excluding the header) to fill the 2D list
    for line in lines[1:]:  # Skip header
        row = line.strip().split(",")
        point_id = int(row[0]) - 1  # Adjust for 0-indexing

        for i in range(1, len(row)):
            if row[i]:  # If there's a distance value
                distance = float(row[i])
                distance_matrix[point_id][i - 1] = distance
                distance_matrix[i - 1][
                    point_id
                ] = distance  # Mirror the distance for bi-directionality

    return distance_matrix


def loadAddressData(file_path):
    """
    Load address data from the specified file path and return it as a list of dictionaries.

    Parameters:
    file_path (str): The path to the file containing the address data.

    Returns:
    list: A list of dictionaries representing the address data.
    """
    addressdata = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            headers = file.readline().strip().split(",")
            for line in file:
                values = line.strip().split(",")
                row_data = {header: value for header, value in zip(headers, values)}
                addressdata.append(row_data)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []  # Return an empty list or handle the error as appropriate

    return addressdata


try:
    distanceData = loadDistanceData(DISTANCE_FILE)
    addressData = loadAddressData(ADDRESS_FILE)
    if Debug:
        print(distanceData)
        print(addressData)
except FileNotFoundError as e:
    print(f"Error: The file {e.filename} was not found.")
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
        if Debug:
            print(f"Calculating distance between {index1} & {index2}")
        return float(distance_data[index1][index2])
    except IndexError:
        print(
            f"     ERROR:One or both of the provided indices are out of bounds.\n"
            f"    {index1} & {index2}"
        )
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
    unsorted_packages = [
        PackageHashTable.search(package_id) for package_id in truck.load
    ]
    truck.load.clear()  # Clear the truck's load for re-loading sorted packages
    for package in unsorted_packages:
        package.status = "En Route"
        package.truck = f"Truck #{truck.Id}"  # Update package's truck ID
        package.loadTime = truck.departure_time  # Update package's load time
    while unsorted_packages:
        # Find the next closest package to the current truck location
        closest_package, closest_distance = find_closest_package(
            truck.location, unsorted_packages, distance_data
        )

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
    closest_distance = float("inf")  # Initialize with infinity

    for package in packages:  # Iterate over the list of packages
        distance = distanceBetween(
            current_location, package.destination_index, distance_data
        )  # Calculate the distance
        if distance < closest_distance:  # Update the closest package and distance
            closest_package, closest_distance = (
                package,
                distance,
            )  # Update the closest package

    return closest_package, closest_distance  # Return the closest package


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

    package.delivery_time = truck.time
    package.status = "Delivered"
    on_time_check(package)
    if Debug:
        print(f"Delivered Package {package.formatpackagedetails()}")


def calculate_delivery_time(distance, speed):
    """Calculate delivery time given distance and speed, returning a timedelta object."""
    return datetime.timedelta(hours=distance / speed)

def on_time_check(package):
    if package.deadline_time == "EOD":
        deadline_time = datetime.timedelta(hours=17)  # 5 PM
    else:
        deadline_time = convert_time_str(package.deadline_time)

    # Check if the package delivery time is after the deadline
    if package.delivery_time > deadline_time:
        print(f"Package# {package.package_id} is late")
        print(f"""Deadline: {package.deadline_time} - Delivery: {package.delivery_time}""")
    else:
        if Debug:
            print(f"Package# {package.package_id}  is on time")
            print(f"""Deadline: {package.deadline_time} - Delivery: {package.delivery_time}""")

def convert_time_str(time_str):
    """Convert deadline time string to datetime object."""
    if time_str == "EOD":
        return datetime.timedelta(hours=17)  # 5 PM

    # Split the time string by space to separate the time and the AM/PM part
    time_part, am_pm = time_str.split()

    # Split the time part by ":" to get hours and minutes
    hours, minutes = map(int, time_part.split(":"))

    # Adjust hours for PM times
    if am_pm.upper() == 'PM' and hours != 12:
        hours += 12
    elif am_pm.upper() == 'AM' and hours == 12:
        hours = 0  # Midnight is represented as 0 hours in 24-hour time format

    # Create timedelta object
    datetime_time = datetime.timedelta(hours=hours, minutes=minutes)
    return datetime_time
def get_time_input():
    """
    A function that prompts the user to input a time in the format HH:MM:SS,
    validates the input, and returns a datetime.timedelta object representing the input time.
    """
    print("Please Enter a time for the lookup. In format HH:MM:SS \n example: 12:00:00")
    while True:  # Loop until a valid time is entered
        try:  # Try to convert the input to a datetime.timedelta object
            print("Enter Time: ")  # Prompt the user to enter a time
            time_input = input()  # Get user input
            hours, minutes, seconds = map(
                int, time_input.split(":")
            )  # Split the input into hours, minutes, and seconds
            time_delta = datetime.timedelta(
                hours=hours, minutes=minutes, seconds=seconds
            )  # Create a timedelta object from the input
            return time_delta  # Return the timedelta object

        except ValueError:
            # Handle the case where the input format is incorrect
            print("Invalid input format. Please use the format HH:MM:SS")


def get_all_package_ids(hash_table):
    """
    Get all package IDs from the hash table.
    Args:
    hash_table: Hash table containing the package IDs.
    Returns:
    List of all package IDs.
    """
    package_ids = []
    for bucket in hash_table.table:  # Iterate through each bucket in the hash table
        for (
            key_value_pair
        ) in bucket:  # Iterate through each key-value pair in the bucket
            package_id = key_value_pair[0]  # Assuming package_id is stored as the key
            package_ids.append(package_id)  # Append the package ID to the list
    return package_ids  # Return the list of all package IDs


class Main:
    """
    The Main class contains the main logic for loading package data, optimizing delivery routes for three trucks,
    and providing a user interface for package reports.

    Attributes:
    - PACKAGE_FILE: The file containing package data
    - PackageHashTable: The hash table used to store package data
    - truck1, truck2, truck3: Instances of the truck class representing the three delivery trucks
    - distanceData: Data structure containing distance information for delivery routes

    Methods:
    - loadPackageData: Loads package data from PACKAGE_FILE into PackageHashTable
    - optimized_delivery: Optimizes the delivery route for a given truck using distanceData
    - get_time_input: Helper function to get user input for time
    - get_all_package_ids: Retrieves all package IDs from PackageHashTable
    """
    # Load CSV_Package into hash table
    loadPackageData(PACKAGE_FILE, PackageHashTable)
    optimized_delivery(truck1, distanceData)
    optimized_delivery(truck2, distanceData)
    if Debug:
        print(truck1.time, truck2.time)
    Truck3_Departure = min(
        truck1.time, truck2.time
    )  # Keep truck 3 at Hub until Truck 1 or 2 finish
    if Debug:
        print(Truck3_Departure)
    optimized_delivery(truck3, distanceData)

    # User Interface for package reports
    print("Loading Package Data")
    print("\nWestern Governors University Parcel Service (WGUPS)")

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
            time_delta = get_time_input()
            print(time_delta)
            print("Enter Package ID Number")
            # User inputs package ID as an integer
            package_id = int(input())
            # Lookup package by ID in hash table
            package = PackageHashTable.search(package_id)
            # Run solo package status report
            if package:
                print(package.packageReport("status", time_delta))
                # package.packageReport("status", time_delta)
                input("Press Enter to Continue...")
            else:
                print("Package Not Found")
        # Lookup package status by time
        elif user_input == "2":
            time_delta = get_time_input()
            print(time_delta)
            all_package_ids = get_all_package_ids(PackageHashTable)
            for package_id in all_package_ids:  # Loop through all packages (
                package = PackageHashTable.search(package_id)
                print(package.packageReport("time", time_delta))
            input("Press Enter to Continue...")
        # Exit Program
        elif user_input == "3":
            isExit = False
        else:
            print(f"\nInvalid input: {user_input}")
