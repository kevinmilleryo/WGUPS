# #Kevin Miller
# #Student ID: 011482203
import csv
import datetime
from HashTable import HashTable
from Package import Package
from Truck import Truck  # Assuming Truck is in a separate module

# read distance csv
with open("distances.csv") as csvfile:
    Distance_CSV = csv.reader(csvfile)
    Distance_CSV = list(Distance_CSV)

# read address csv
with open("addresses.csv") as csvfile1:
    Address_CSV = csv.reader(csvfile1)
    Address_CSV = list(Address_CSV)

# read package csv
with open("packages.csv") as csvfile2:
    Package_CSV = csv.reader(csvfile2)
    Package_CSV = list(csvfile2)

# create object for packages from csv and insert packages
def load_package_data(filename, package_hash):
    with open(filename) as package_info:
        package_data = csv.reader(package_info)
        for package in package_data:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pStatus = "At hub"

            p = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline, pWeight, pStatus)

            package_hash.insert(pID, p)

# calculate distance
def find_distance(x, y):
    distance = Distance_CSV[x][y]
    if distance == '':
        distance = Distance_CSV[y][x]

    return float(distance)

# get address number
def get_address(address):
    for row in Address_CSV:
        if address in row[2]:
            return int(row[0])

# Create and load 3 trucks
truck1 = Truck(16, 18, None, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
               datetime.timedelta(hours=8))

truck2 = Truck(16, 18, None, [3, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
               "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))

truck3 = Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
               datetime.timedelta(hours=10, minutes=20))

# create hash table
package_hash = HashTable()

# load packages into hash
load_package_data("packages.csv", package_hash)

# Iterate through packages and set delivery_truck attribute
for package_id in truck1.packages:
    package = package_hash.lookup(package_id)
    package.delivery_truck = 1

for package_id in truck2.packages:
    package = package_hash.lookup(package_id)
    package.delivery_truck = 2

for package_id in truck3.packages:
    package = package_hash.lookup(package_id)
    package.delivery_truck = 3

# deliver packages utilizing the nearest neighbor algorithm
def deliver_packages(truck):
    # put all packages into an array of undelivereds
    undelivered = []
    for packageID in truck.packages:
        package = package_hash.lookup(packageID)
        undelivered.append(package)
        # clear the package list of the truck
    truck.packages.clear()

    # Loop through undelivered packages until none remain
    while len(undelivered) > 0:
        next_address = 2000
        next_package = None
        for package in undelivered:
            if find_distance(get_address(truck.address), get_address(package.address)) <= next_address:
                next_address = find_distance(get_address(truck.address), get_address(package.address))
                next_package = package
        # add the closest package to the truck list
        truck.packages.append(next_package.ID)
        # remove that package from undelivered
        undelivered.remove(next_package)
        # add mileage driven to truck mileage
        truck.mileage += next_address
        # update the truck address
        truck.address = next_package.address
        # add time to get to the package to the truck time
        truck.time += datetime.timedelta(hours=next_address / 18)
        next_package.delivery = truck.time
        next_package.departure = truck.departure


# load trucks
deliver_packages(truck1)
deliver_packages(truck2)
# truck 3 leaves last
update_time = datetime.timedelta(hours=10, minutes=20)
# Check if the departure time of truck3 is after 10:20 a.m.
if truck3.departure >= update_time:
    # Update the address for Package #9
    package_9 = package_hash.lookup(9)
    package_9.address = "410 S State St"
    package_9.zipcode = "84111"
deliver_packages(truck3)



#User interface
class Main:
    print("Package service go brrrrrrr")
    #truck mileage
    print("Truck 1 mileage: " + str(round(truck1.mileage,1)))
    print("Truck 2 mileage: " + str(truck2.mileage))
    print("Truck 3 mileage: " + str(truck3.mileage))
    #total mileage for all trucks
    print("Total mileage: " + str(truck1.mileage + truck2.mileage + truck3.mileage))
    #ask user for input to start program
    user_input = input("Input 'start' to begin: ")
    if user_input == "start":
        try:
            #ask to input time
            user_time = input("Input a time (HH:MM:SS) to check package status: ")
            (h, m, s) = user_time.split(":")
            convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            # ask user if they want to see all or single package
            user_input2 = input("To view single package status, input 'single', for all packages, input 'all': ")
            if user_input2 == "single":
                try:
                    # ask for package id if they want to see a single package status
                    input_single = input("Input package ID: ")
                    package = package_hash.lookup(int(input_single))
                    package.update_status(convert_timedelta)
                    print(str(package))
                except ValueError:
                    print("Invalid input, exiting program")
                    exit()
            # display all package information if input is "all"
            elif user_input2 == "all":
                try:
                    for packageID in range(1, 41):
                        package = package_hash.lookup(packageID)
                        package.update_status(convert_timedelta)
                        print(str(package))
                except ValueError:
                    print("Invalid input, exiting program")
                    exit()
            else:
                exit()
        except ValueError:
            print("Invalid input, exiting program")
            exit()
    elif user_input != "start":
        print("Invalid input, exiting program")
        exit()