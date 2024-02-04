# Author: Alex Fair
# Student ID:
# Title:

import csv, datetime
from builtins import ValueError

# Define file path constants
DISTANCE_FILE = "CSV/distances.csv"
ADDRESS_FILE = "CSV/addresses.csv"
PACKAGE_FILE = "CSV/packages.csv"


# Define a function to read CSV files
def read_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)


# Read the distance information file
CSV_Distance = read_csv(DISTANCE_FILE)

# Read the address information file
CSV_Address = read_csv(ADDRESS_FILE)

# Read the package information file
CSV_Package = read_csv(PACKAGE_FILE)
