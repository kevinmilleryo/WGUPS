#Kevin Miller
#Student ID: 011482203

import csv
import datetime
import Truck
from builtins import ValueError

from HashTable import HashTable
from Package import Package

#create hash table
package_hash = HashTable()


#read distance csv
with open("distances.csv") as csvfile:
    Distance_CSV = csv.reader(csvfile)
    Distance_CSV = list(Distance_CSV)

#read address csv
with open("addresses.csv") as csvfile1:
    Address_CSV = csv.reader(csvfile1)
    Address_CSV = list(Address_CSV)

#read package csv
with open("packages.csv") as csvfile2:
    Package_CSV = csv.reader(csvfile2)
    Package_CSV = list(csvfile2)

#create object for packages from csv and insert packages
def load_package_data(filename, package_hash):
    with open(filename) as package_info:
        package_data = csv.reader(package_info)
        for package in package_data:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[3]
            pDeadline = package[5]
            pWeight = package[6]
            pStatus = "At hub"

            p = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline, pWeight, pStatus)

            package_hash.insert(pID, p)

#calculate distance
def find_distance(x,y):
    distance = Distance_CSV[x][y]
    if distance == '':
        distance = Distance_CSV[y][x]

    return float(distance)

#get address number
def get_address(address):
    for row in Address_CSV:
        if address in row[2]:
            return int(row[0])

#load packages into hash
load_package_data("packages.csv", package_hash)

#Create and load 3 trucks
truck1 = Truck.Truck(16, 18, None, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))

# Iterate through packages and set delivery_truck attribute
for package_id in truck1.packages:
    package = package_hash.lookup(package_id)
    package.delivery_truck = 1

truck2 = Truck.Truck(16, 18, None, [3, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

# Iterate through packages and set delivery_truck attribute
for package_id in truck2.packages:
    package = package_hash.lookup(package_id)
    package.delivery_truck = 2

truck3 = Truck.Truck(16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=9, minutes=5))

# Iterate through packages and set delivery_truck attribute
for package_id in truck3.packages:
    package = package_hash.lookup(package_id)
    package.delivery_truck = 3


#deliver packages utilizing nearest neighbor algorithm
def deliver_packages(truck):
    #put all packages into array of undelivereds
    undelivered = []
    for packageID in truck.packages:
        package = package_hash.lookup(packageID)
        undelivered.append(package)
        #clear package list of truck
    truck.packages.clear()

#Loop through undelivered packages until none remain
    while len(undelivered) > 0:
        next_address = 2000
        next_package = None
        for package in undelivered:
            if find_distance(get_address(truck.address), get_address(package.address)) <= next_address:
                next_address = find_distance(get_address(truck.address), get_address(package.address))
                next_package = package
        #add closest package to truck list
        truck.packages.append(next_package.ID)
        #remove that package from undelivered
        undelivered.remove(next_package)
        #add mileage driven to truck mileage
        truck.mileage += next_address
        #update truck address
        truck.address = next_package.address
        #add time to get to package to truck time
        truck.time += datetime.timedelta(hours=next_address / 18)
        next_package.delivery = truck.time
        next_package.departure = truck.departure

# load trucks
deliver_packages(truck1)
deliver_packages(truck2)
#truck 3 leaves last
truck3.depart = min(truck1.time, truck2.time)
deliver_packages(truck3)

#User interface


class Main:
    print("Package service go brrrrrrr")
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

# import csv
# import re
# import Package
# import HashTable
# import Truck
#
#
# def create_packages_hash_table():
#     packages_hash_table = HashTable.HashTable()
#
#     # Read packages.csv
#     with open('packages.csv', mode='r', encoding='utf-8-sig') as csv_packages_file:
#         csv_packages = csv.reader(csv_packages_file, delimiter=',')
#         csv_packages = list(csv_packages)
#
#         # Add packages to hash table
#         for package in csv_packages:
#             package_id = package[0]
#             package_address = package[1]
#             package_city = package[2]
#             package_state = package[3]
#             package_zip = package[4]
#             package_deadline = package[5]
#             package_weight = package[6]
#             package_note = package[7]
#             packages_hash_table.add(package_id, Package.Package(package_id, package_address, package_city,
#                                     package_state, package_zip, package_deadline, package_weight, package_note))
#
#     return packages_hash_table
#
# # Create address list
# def create_addresses_list():
#     with open('addresses.csv', mode='r', encoding='utf-8-sig') as csv_addresses_file:
#         csv_addresses = csv.reader(csv_addresses_file)
#         return list(csv_addresses)
#
# # Create distances list
# def create_distances_list():
#     with open('distances.csv', mode='r', encoding='utf-8-sig') as csv_distances_file:
#         csv_distances = csv.reader(csv_distances_file)
#         return list(csv_distances)
#
#
# # Create packages hash table
# packages_hash_table = create_packages_hash_table()
#
# # Create addresses list
# addresses_list = create_addresses_list()
#
# # Create distances list
# distances_list = create_distances_list()
#
#
# # Create and load first truck
# first_truck = Truck.Truck(
#     1, 16, ["1", "2", "4", "5", "13", "14", "15", "16", "19", "20", "29", "30", "31", "34", "37", "40"], 0, 0, "4001 South 700 East", "Salt Lake City", "UT", "84107")
#
# # Set package truck id to 1
# for package in first_truck.packages:
#     packages_hash_table.get(package).delivery_truck = 1
#
# # Create and load second truck
# second_truck = Truck.Truck(
#     2, 16, ["3", "6", "7", "8", "10", "11", "12", "17", "18", "21", "22", "28", "32", "36", "38", "39"], 0, 0, "4001 South 700 East", "Salt Lake City", "UT", "84107")
#
# # Set package truck id to 2
# for package in second_truck.packages:
#     packages_hash_table.get(package).delivery_truck = 2
#
# # Create and load third truck
# third_truck = Truck.Truck(
#     3, 16, ["9", "23", "24", "25", "26", "27", "33", "35", "39"], 0, 0, "4001 South 700 East", "Salt Lake City", "UT", "84107")
#
# # Set package truck id to 3
# for package in third_truck.packages:
#     packages_hash_table.get(package).delivery_truck = 3
#
# # Get address id from address csv
# def get_address_id(address):
#     for item in addresses_list:
#         if address in item[2]:
#             return int(item[0])
#
# # Get distance between two addresses
# def get_distance(start_address, end_address):
#     start_address_id = get_address_id(start_address)
#     end_address_id = get_address_id(end_address)
#     distance = distances_list[start_address_id][end_address_id]
#     if distance == "":
#         return float(distances_list[end_address_id][start_address_id])
#     return float(distances_list[start_address_id][end_address_id])
#
# # Method for delivering packages on trucks
# def deliver_packages(truck):
#     # Set current address to hub
#     current_address = truck.current_address
#
#     # If truck 1, set departure offset time as 8:00 AM
#     if truck.id == 1:
#         truck.float_time += 480
#     # If truck 2, set departure offset time as 9:05 AM
#     elif truck.id == 2:
#         truck.float_time += 545
#
#     # Print truck id
#     print("Delivering packages on truck " + str(truck.id) +
#           " at " + '{0:02.0f}:{1:02.0f}'.format(
#         *divmod(truck.float_time, 60)) + "...")
#
#     # Correct package 9 address for truck 3
#     if truck.id == 3:
#         print("\tCorrecting package 9 address to 410 S State St...")
#         packages_hash_table.get("9").address = "410 S State St"
#         packages_hash_table.get("9").city = "Salt Lake City"
#         packages_hash_table.get("9").state = "UT"
#         packages_hash_table.get("9").zip = "84111"
#
#     # Set package status to "en route"
#     for package in truck.packages:
#         packages_hash_table.get(package).status = "en route"
#
#     # Deliver packages
#     while truck.packages:
#         # Get shortest distance between current address and next package
#         shortest = 1000
#         next_package = ""
#         for package in truck.packages:
#             if shortest > get_distance(current_address, packages_hash_table.get(package).address):
#                 shortest = get_distance(
#                     current_address, packages_hash_table.get(package).address)
#                 next_package = package
#
#         # Add distance to package delivery distance
#         packages_hash_table.get(next_package).delivery_distance += shortest
#         # Add distance to truck distance
#         truck.distance += shortest
#         # Calculate time
#         time = (shortest / 18) * 60
#         # Add time to truck float time
#         truck.float_time += time
#         # Set package status to "Delivered"
#         packages_hash_table.get(next_package).status = "delivered"
#         # Set package delivery time
#         # Convert float time
#         package_delivery_time = '{0:02.0f}:{1:02.0f}'.format(
#             *divmod(truck.float_time, 60))
#         packages_hash_table.get(
#             next_package).delivery_time = package_delivery_time
#         # Deliver package
#         print("\t" + package_delivery_time + " - Delivering package " + next_package + " at " +
#               packages_hash_table.get(next_package).address + ".")
#         # Remove package from truck
#         truck.packages.remove(next_package)
#         # Set current address to next package address
#         current_address = packages_hash_table.get(next_package).address
#
#     # Print total distance traveled
#     print("\nTruck " + str(truck.id) + " delivered all packages at " +
#           str(round(truck.distance, 2)) + " miles.")
#
#     # Print total time elapsed
#     time = '{0:02.0f}:{1:02.0f}'.format(*divmod(truck.float_time, 60))
#     print("Truck " + str(truck.id) + " delivered all packages at " +
#           time + ".\n")
#
#     # Return total distance traveled
#     return truck.distance
#
#
# # Deliver packages on trucks
# total_distance = 0
# total_distance += deliver_packages(first_truck)
# total_distance += deliver_packages(second_truck)
#
# # Third truck departure
# if first_truck.float_time < second_truck.float_time:
#     third_truck.float_time = first_truck.float_time
# else:
#     third_truck.float_time = second_truck.float_time
# total_distance += deliver_packages(third_truck)
#
# # Print total distance
# print("Total distance traveled: " + str(total_distance) + " miles.")
#
# # Print total time
# time = '{0:02.0f}:{1:02.0f}'.format(
#     *divmod(first_truck.float_time + second_truck.float_time + third_truck.float_time - 1645, 60))
# print("Total time: " + time + ".")
#
# # Line divider
# print("\n" + "*" * 80 + "\n")
#
# # Console interface
# while True:
#     # Package lookup or time lookup
#     lookup_input = input(
#         "Enter 'p' to find PACKAGE by id or 't' to package status at a specific time (HH:MM) 'q' to quit \n> ")
#
#     # Lookup function
#     if lookup_input == "q":
#         break
#     # package
#     if lookup_input == "p":
#         # Package lookup
#         package_id_input = input(
#             "Enter a package ID to look up package \n> ")
#         # valid id
#         if packages_hash_table.get(package_id_input) is not None:
#             # Print package
#             print("\nPackage ID " + package_id_input + ":")
#             print("\tAddress: " + packages_hash_table.get(
#                 package_id_input).address)
#             print("\tDeadline: " + packages_hash_table.get(
#                 package_id_input).deadline)
#             print("\tCity: " + packages_hash_table.get(
#                 package_id_input).city)
#             print("\tState: " + packages_hash_table.get(
#                 package_id_input).state)
#             print("\tZip: " + packages_hash_table.get(
#                 package_id_input).zip)
#             print("\tWeight: " + packages_hash_table.get(
#                 package_id_input).weight)
#             print("\tStatus: " + packages_hash_table.get(
#                 package_id_input).status)
#             print("\tDelivery time: " + packages_hash_table.get(
#                 package_id_input).delivery_time)
#         else:
#             print("Invalid ID")
#
#
#     # Time
#     elif lookup_input == "t":
#         # Get input
#         time_input = input(
#             "Enter a time (HH:MM) to show all package statuses and distance traveled across all trucks \n> ")
#         # total distance traveled
#         total_distance = 0
#         # perform time lookup
#         if re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d$", time_input):
#             # user input to float
#             time_input = time_input.split(":")
#             time_input = (int(time_input[0]) * 60) + int(time_input[1])
#
#             # Print all package statuses on all trucks
#             print("\nPackage statuses at " + '{0:02.0f}:{1:02.0f}'.format(
#                 *divmod(time_input, 60)) + ":")
#             for package in range(1, packages_hash_table.size + 1):
#                 str_package = str(package)
#                 if packages_hash_table.get(str_package) is not None:
#                     if packages_hash_table.get(str_package).delivery_time != "N/A":
#                         delivery_time = packages_hash_table.get(
#                             str_package).delivery_time
#                         delivery_time = delivery_time.split(":")
#                         delivery_time = (
#                             int(delivery_time[0]) * 60) + int(delivery_time[1])
#                         if delivery_time <= time_input:
#                             print("\tPackage " + str_package + " - " +
#                                   packages_hash_table.get(str_package).status + " at " + packages_hash_table.get(str_package).delivery_time +
#                                   " by truck " + str(packages_hash_table.get(str_package).delivery_truck) + " to " +
#                                   addresses_list[int(get_address_id(packages_hash_table.get(str_package).address))][1] +
#                                   ", " + packages_hash_table.get(str_package).address + ".")
#                             total_distance += packages_hash_table.get(
#                                 str_package).delivery_distance
#                         # If package delivery time is greater than user input time
#                         else:
#                             # If input is less than 8:00 all packages are at hub
#                             if time_input < 480:
#                                 print("\tPackage " + str_package + " - at hub " + " on truck " +
#                                       str(packages_hash_table.get(str_package).delivery_truck) + " at " +
#                                       addresses_list[0][1] + ", " + addresses_list[0][2] + ".")
#                             # If input is equal to or greater than 8:00 but less than 9:05
#                             elif time_input >= 480 and time_input < 545:
#                                 # Truck 1 packages
#                                 if packages_hash_table.get(str_package).delivery_truck == 1:
#                                     print("\tPackage " + str_package + " - en route on truck " +
#                                           addresses_list[int(get_address_id(packages_hash_table.get(str_package).address))][1] +
#                                           ", " + str(packages_hash_table.get(str_package).delivery_truck) + " to " +
#                                           packages_hash_table.get(str_package).address + ".")
#                                 # All others packages are at hub
#                                 else:
#                                     print("\tPackage " + str_package + " - at hub on truck " +
#                                           str(packages_hash_table.get(str_package).delivery_truck) + " at " +
#                                           addresses_list[0][1] + ", " + addresses_list[0][2] + ".")
#                             # If input is equal to or greater than 9:05 but less than 10:20
#                             elif time_input >= 545 and time_input < 620:
#                                 # Truck 2 en route
#                                 if packages_hash_table.get(str_package).delivery_truck == 2:
#                                     print("\tPackage " + str_package + " - en route on truck " +
#                                           addresses_list[int(get_address_id(packages_hash_table.get(str_package).address))][1] +
#                                           ", " + str(packages_hash_table.get(str_package).delivery_truck) + " to " +
#                                           packages_hash_table.get(str_package).address + ".")
#                                 # All other packages are at hub
#                                 else:
#                                     print("\tPackage " + str_package + " - at hub on truck " +
#                                           str(packages_hash_table.get(str_package).delivery_truck) + " at " +
#                                           addresses_list[0][1] + ", " + addresses_list[0][2] + ".")
#                             # If input is equal to or greater than whenever truck 3 departure
#                             elif time_input >= third_truck.float_time:
#                                 # Truck 3 en route
#                                 if packages_hash_table.get(str_package).delivery_truck == 3:
#                                     print("\tPackage " + str_package + " - en route on truck " +
#                                           addresses_list[int(get_address_id(packages_hash_table.get(str_package).address))][1] +
#                                           ", " + str(packages_hash_table.get(str_package).delivery_truck) + " to " +
#                                           packages_hash_table.get(str_package).address + ".")
#                                 # All other packages are at hub
#                                 else:
#                                     print("\tPackage " + str_package + " - at hub on truck " +
#                                           str(packages_hash_table.get(str_package).delivery_truck) + " at " +
#                                           addresses_list[0][1] + ", " + addresses_list[0][2] + ".")
#             # Print total distance
#             print("\nTotal distance traveled at " +
#                   '{0:02.0f}:{1:02.0f}'.format(
#                       *divmod(time_input, 60)) + " is " + str(round(total_distance, 2)) + " miles.")
#         # If input is invalid
#         else:
#             print("Invalid time. Please try again.")
#
#     # Line divider
#     print("\n" + "*" * 80 + "\n")
