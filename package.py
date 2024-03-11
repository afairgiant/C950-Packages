# Class representing packages
import datetime
from datetime import timedelta

"""
This file contains the Package class, which represents the packages
that will be delivered.
"""
Debug = False


class Package:
    """
    Initializes the package with the given parameters.

    Args:
        package_id (int): The unique ID of the package.
        address (str): The address of the package.
        city (str): The city of the package.
        state (str): The state of the package.
        zipcode (str): The zip code of the package.
        deadline_time (str): The deadline time of the package.
        weight (str): The weight of the package in kg.
        status (str): The status of the package (e.g., at hub, loaded, en route, delivered).
        note (str): The note related to the package.
        destination_index (int): The index of the destination.
        truck (str): The truck assigned to the package.
        loadTime (str): The load time of the package.
    """

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
            loadTime,
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
        self.truck = None  # Only used when loaded
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
        """
        Updates the status of the package based on the current time.

        Parameters:
        current_datetime (datetime): The current date and time.

        Returns:
        None
        """
        loadTime = self.loadTime

        # Update package status
        if current_datetime < loadTime:
            # Account for packages delayed on flight in
            if self.package_id in [6, 25, 28, 32]:
                self.status = "Delayed on flight"
            else:
                self.status = "At Hub"
        elif current_datetime == loadTime:
            self.status = "Loaded on " + self.truck
        elif loadTime < current_datetime < self.delivery_time:
            self.status = "En Route on " + self.truck
        elif current_datetime > self.delivery_time:
            self.status = "Delivered"
        else:
            self.status = "Contact Support"

    def formatpackagedetails(self):
        """
        Returns a formatted string containing the details of the package.

        The details include the package ID, delivery address, delivery deadline,
        delivery city, delivery zip code, package weight, delivery status, and delivery time.

        Returns:
            str: A string containing the details of the package.
        """
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
        """
        Reports the delivery time of the package based on the current date and time.

        Parameters:
            current_datetime (datetime): The current date and time.

        Returns:
            str: A string containing the delivery time of the package.
            If the package has been delivered, the delivery time is returned. Otherwise, the estimated delivery time is returned.
        """
        if self.delivery_time < current_datetime:
            if Debug:
                print("Package has been delivered")
            report_delivery_time = f"Delivered at: {self.delivery_time} on {self.truck}"

        else:
            if Debug:
                print("Package has not been delivered")
            # If package hasn't been delivered show estimated time
            report_delivery_time = f"Estimated Delivery Time: {self.delivery_time} on {self.truck}"

        return report_delivery_time

    def packageReport(self, reportType, current_datetime):
        """
        Report the package details based on the specified report type.

        Parameters:
            reportType (str): The type of report to generate. Valid options are "status" and "time".
            current_datetime (datetime): The current date and time.

        Returns:
            str: A formatted string containing the package details based on the specified report type.
        """
        # Report package status
        reportDelivery = self.reportDeliveryTime(current_datetime)
        self.status_update(current_datetime)

        if reportType == "status":
            status_report = (f"\033[4mPackage Report for Package #{self.package_id}\033[0m\n"
                             f"Package ID: {self.package_id}\n"
                             f"Delivery Deadline: {self.deadline_time}\n"
                             f"Delivery Address: {self.address}\n"
                             f"Delivery City: {self.city}\n"
                             f"Delivery Zip Code: {self.zipcode}\n"
                             f"Package Weight: {self.weight}\n"
                             f"Delivery Status: {self.status}\n"
                             f"{reportDelivery}")

            return status_report

        elif reportType == "time":
            time_report = (f"Package ID: {self.package_id}\n"
                           f"   Delivery Deadline: {self.deadline_time}\n"
                           f"   Delivery Address: {self.address} {self.city} {self.zipcode}\n"
                           f"   Delivery Status: {self.status}.\n"
                           f"   {reportDelivery}"
                           )

            return time_report

        elif reportType == "truck":
            return (
                f"\033[fmPackage Report for Truck #"
                # TODO: create a report to show status of packages per truck at a given time.
            )
        else:
            print("Houston we have a problem...")
