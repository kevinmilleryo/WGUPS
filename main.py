import datetime

from HashTable import HashTable
from Package import Package
from Truck import Truck
import csv

package_hash = HashTable()
package_ids = []

# Read the data from packages.csv
with open('packages.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    packages = list(reader)

# Read the data from distances.csv
with open('distances.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    distances = list(reader)

# Use the data from the packages.csv file to populate hash table
def populate_package_hash():
    for row in packages:
        p = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], "At the hub")
        package_ids.append(int(p.id))
        package_hash.insert(int(p.id), p)

# Find the address index in the distances.csv file
def find_address(address):
    i = 0
    for col in distances[0]:
        if address in col:
            return i
        i = i + 1

# Nearest neighbor algorithm
def calculate_route(truck, end_time):
    undelivered_packages = truck.packages.copy()
    # Do not run if the truck will not have departed
    if end_time >= truck.current_time:

        # Change the status of each package on the truck to "En route"
        for package_id in truck.packages:
            package = package_hash.search(package_id)
            package.status = "En Route by " + truck.name

        # Iterate through all undelivered packages
        while len(undelivered_packages) > 0:
            least_distance = 1000.0
            next_package = None


            # find next delivery address closest to the truck location
            for package_id in undelivered_packages:

                # Find indexes for current address of truck and the address of the next package
                curr_loc = int(find_address(truck.current_location))
                package = package_hash.search(package_id)
                next_loc = int(find_address(package.address))

                # The order of the location indexes to get the distance depends on which index is greater
                if (next_loc > curr_loc):
                    distance = float(distances[next_loc][curr_loc])
                else:
                    distance = float(distances[curr_loc][next_loc])

                # If distance between addresses is less than the least distance found
                # set new least distance and next package
                if (distance < least_distance):
                    next_package = package
                    least_distance = distance

            # Mark a package as "delivered", removing from undelivered packages
            undelivered_packages.remove(int(next_package.id))

            # Update time by estimating the time it takes to deliver the next package
            truck.current_time = truck.current_time + datetime.timedelta(hours=(least_distance / truck.speed))

            # If current time has gone past end time, set the current time and break loop
            if (truck.current_time > end_time):
                truck.current_time = end_time
                break;

            next_package.status = "Delivered @ " + str(truck.current_time) + " by " + truck.name

            package_hash.insert(int(next_package.id), next_package)

            truck.current_location = next_package.address

            truck.distance += least_distance
    return truck


if __name__ == '__main__':


    while True:
        # Populate hash table from package CSV
        package_ids = []
        populate_package_hash()

        # Create trucks and load packages
        truck1_packages = [1, 13, 14, 15, 16, 19, 20, 23, 29, 30, 31, 34, 37, 40]
        truck1 = Truck("Truck 1", 18, datetime.timedelta(hours=8), truck1_packages, "4001 South 700 East")
        truck2_packages = [2, 3, 4, 5, 6, 10, 18, 21, 22, 26, 35, 36, 38]
        truck2 = Truck("Truck 2", 18, datetime.timedelta(hours=9, minutes=15), truck2_packages, "4001 South 700 East")
        truck3_packages = [7, 8, 9, 11, 12, 17, 24, 25, 27, 28, 32, 33, 39]
        truck3 = Truck("Truck 3", 18, datetime.timedelta(hours=10, minutes=30), truck3_packages, "4001 South 700 East")

        # Menu
        print("\n****************************************************************************\n" +
              "p: Print all package staus and total mileage\n" +
              "s [package_id] [time] : Get single package status and (military) time\n" +
              "a [time]: Get all packages with (military) time\n" +
              "q: Quit Program\n" +
              "******************************************************************************")
        command = input("\ncommand: ").split(" ")

        if command[0] == "p":

            # Set end time to "EOD"
            time = datetime.timedelta(hours=23)

            # Because this command prints for EOD, the package with the wrong address would be updated
            p = package_hash.search(9)
            p.address = "410 S State St"
            p.city = "Salt Lake City"
            p.state = "UT"
            p.zip = "84111"
            package_hash.insert(p.id, p)

            # Find status of packages
            truck1 = calculate_route(truck1, time)

            truck2 = calculate_route(truck2, time)

            truck3 = calculate_route(truck3, time)

            # Print package info
            print("Package ID, Address, City, State, Zip, Delivery Deadline, Weight (kg), Notes, Status")
            for id in package_ids:
                package = package_hash.search(id)
                print(package)
            print("Distance traveled: " + str(round(truck1.distance + truck2.distance + truck3.distance, 2)))

        elif command[0] == "s":
            # Ask for parameters if not given
            if (len(command) < 3):
                print("Please provide both inputs")
                continue
            # Get id and time from input
            package_id = int(command[1])
            time_param = command[2].split(":")
            time = datetime.timedelta(hours=int(time_param[0]), minutes=int(time_param[1]))

            # Updated 9 with correct address if past 10:20
            if time >= datetime.timedelta(hours=10, minutes=20):
                p = package_hash.search(9)
                p.address = "410 S State St"
                p.city = "Salt Lake City"
                p.state = "UT"
                p.zip = "84111"
                package_hash.insert(p.id, p)

            # Find what the statuses are of all the packages by the given time
            truck1 = calculate_route(truck1, time)

            truck2 = calculate_route(truck2, time)

            truck3 = calculate_route(truck3, time)

            # Print package info
            print("Package ID, Address, City, State, Zip, Delivery Deadline, Weight (kg), Notes, Status")
            package = package_hash.search(package_id)
            print(package)

        elif command[0] == "a":
            # Request time if not given
            if (len(command) < 2):
                print("Please specify a time")
                continue

            # Get hours and minutes from input
            time_param = command[1].split(":")
            time = datetime.timedelta(hours=int(time_param[0]), minutes=int(time_param[1]))

            # Updated package 9 if time is past 10:20
            if time >= datetime.timedelta(hours=10, minutes=20):
                p = package_hash.search(9)
                p.address = "410 S State St"
                p.city = "Salt Lake City"
                p.state = "UT"
                p.zip = "84111"
                package_hash.insert(p.id, p)

            # Check status of trucks
            truck1 = calculate_route(truck1, time)

            truck2 = calculate_route(truck2, time)

            truck3 = calculate_route(truck3, time)

            # Print package info
            print("Package ID, Address, City, State, Zip, Delivery Deadline, Weight (kg), Notes, Status")
            for id in package_ids:
                package = package_hash.search(id)
                print(package)

        # Quit
        else:
            break