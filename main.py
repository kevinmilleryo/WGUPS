from hashmap import HashMap
from package import Package
from truck import Truck

import csv

package_hash = HashMap()
package_ids = []

# Read CSV files
with open("WGUPS Distance Table.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    distance = [row for row in reader]

with open("WGUPS Package File.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    package = [row for row in reader]

# Populate packages
def populate_package_hash():
    for row in package:
        p = Package(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], "At the hub")
        package_ids.append(int(p.id))
        package_hash.insert(int(p.id), p)

# Find the index of an address in the distances table
def find_address(address):
    i = 0
    for col in distance[0]:
        if address in col:
            return i
        i = i + 1
