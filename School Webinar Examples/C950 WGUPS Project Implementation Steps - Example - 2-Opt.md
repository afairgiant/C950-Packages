 C950 WGUPS Project Implementation Steps - Example - 2-Opt

 

'''

C950 WGUPS Project - Implementation Steps - Start

Please note; this is an example of implementation utilizing 2-Opt Algorithm.

Feel free to use it by citing this document, however it is highly recommended that you come up with your own approach

---------------------------------------------------------------------------------------------

A) Package data steps:

1-Create HashTable data structure (See C950 - Webinar-1 - Let’s Go Hashing webinar)

2-Create Package object and have packageCSV and distanceCSV and addressCSV files ready

3-Create loadPackageData(HashTable) to 

- read packages from packageCSV file (see C950 - Webinar-2 - Getting Greedy, who moved my data  webinar) 

- update Package object

- insert Package object into HashTable with the key=PackageID and Item=Package

 

B) Distance data steps:

B.1) Upload Distances:

4-Create distanceData List

5-Define loadDistanceData(distanceData) to read distanceCSV file 

- read distances from distanceCSV file; row by row

- append row to distanceData (For two-dimensional list and 2-Opt Algorithm, See C950 WGUPS Distance Table Matrix 2-Opt)

B.2) Upload Addresses:

6-Create addressData List 

7-Define loadAddressData(addressData) to read addressCSV file

- read only addresses from addressCSV file

- append address to addressData. 

 

C) Truck Object and Load Packages:

8-Create Truck object and have truck.truckPackages

9-Manually/Heuristically Load Trucks based on assumptions provided (ex. Truck-2 must have some packages, some packages go together, some packages are delayed, ...)

10-Define truckAddressListAndDistanceMatrix(truck) to populate truck.truckDistanceMatrix, truck.truckDistanceAddresses, truck.truckPackagesBestTour for truck.truckPackages per truck.

 

D) Algorithm to Deliver Packages:

D.1) Implement 2-Opt Algorithm

11-Define twoOptDistance(tour,truck.truckDistanceMatrix) to return best distance

12-Define twoOpt(truck.truckDistanceMatrix) to implement 2-opt Algorithm; random initial tour and then to return best distance/best tour and update truck.truckPackagesBestTour 

D.2) Function to return the distance between two addresses:

13-Define distanceBetween(address1, address2)

14-Return distanceData[addressData.index(address1)][addressData.index(address2)]

   i.e. distances between addresses can be accessed via distanceData[i][j]; 

D.3) Function to deliver packages in a Truck:

15-Define truckDeliverPackagesBestTour(truck) to deliver packages 

16-Loop truck.truckPackagesBestTour and call distanceBetween(address1, address2) for all the addresses not visited yet in the truck

D.4) Keep track of miles and time delivered:

17-Update delivery status and time delivered in Hash Table for the package delivered and keep up with total mileage and delivery times. 

    i.e. How to keep track of the time?:

    timeToDeliver(h) = distance(miles)/18(mph) where 18 mph average Truck speed. 

    time_obj = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s)). time_obj could be accumulated to keep track of time.

 

E) UI to Interact with the Users:

18-Create an UI to interact and report the results based on the requirements. 

Possible Menu Options:

***************************************

1. Print All Package Status and Total Mileage       

2. Get a Single Package Status with a Time

3. Get All Package Status with a Time 

4. Exit the Program               

***************************************

 

Possible output example:

PackageID, Address, City, State, Zip, Delivery Deadline, Mass KILO, PageSpecial Notes, Status, DeliveryTime

1, 195 W Oakland Ave, Salt Lake City, UT, 84115, 10:30 AM, 21, , ... Delivered by Truck-2, 08:46:20

2, 2530 S 500 E, Salt Lake City, UT, 84106, EOD, 44, , ... AtHub

3, 233 Canyon Rd, Salt Lake City, UT, 84103, EOD, 2, Can only be on truck 2, ... InRoute by Truck-2

...

...

...

C950 WGUPS Project - Implementation Steps - End

---------------------------------------------------------------------------------------------

'''