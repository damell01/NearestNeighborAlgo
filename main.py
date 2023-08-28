import csv

# Function to load package data from CSV
def load_package_data(csv_filename):
    packages = []
    with open(csv_filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            package_id, delivery_address, city, state, zip_code, delivery_deadline, package_weight, special_note = row
            packages.append({
                'package_id': package_id,
                'delivery_address': delivery_address,
                'city': city,
                'state': state,
                'zip_code': zip_code,
                'delivery_deadline': delivery_deadline,
                'package_weight': package_weight,
                'special_note': special_note
            })
    return packages

# Function to load distance data from CSV
def load_distance_data(csv_filename):
    distances = {}
    with open(csv_filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)
        for row in csvreader:
            location = row[0]
            distances[location] = {}
            for i, distance in enumerate(row[1:], start=1):
                distances[location][headers[i]] = int(distance)
    return distances

# Function to find the nearest neighbor
def find_nearest_neighbor(current_location, undelivered_packages, distance_data):
    nearest_distance = float('inf')
    nearest_package = None
    
    for package in undelivered_packages:
        package_location = package['delivery_address']
        distance = distance_data[current_location][package_location]
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_package = package
    
    return nearest_package['package_id'], nearest_distance

# Main function
def main():
    # Load package data
    package_data = load_package_data('Package_File.csv')

    # Load distance data
    distance_data = load_distance_data('Distance_File.csv')

    # Initialize trucks and packages
    truck1 = []
    truck2 = []
    truck3 = []
    current_location = '0'  # Assuming the hub is labeled as '0' in the distance data

    # Assign packages to trucks using the Nearest Neighbor algorithm
    while package_data:
        nearest_package_id, nearest_distance = find_nearest_neighbor(current_location, package_data, distance_data)
        nearest_package = None

        # Find the package with the nearest_package_id
        for package in package_data:
            if package['package_id'] == nearest_package_id:
                nearest_package = package
                break
        
        if nearest_package:
            current_location = nearest_package['delivery_address']
            if len(truck1) <= len(truck2) and len(truck1) <= len(truck3):
                truck1.append(nearest_package)
            elif len(truck2) <= len(truck3):
                truck2.append(nearest_package)
            else:
                truck3.append(nearest_package)
            package_data.remove(nearest_package)
    
    # Print truck routes
    print("Truck 1 route:")
    for package in truck1:
        print(package)

    print("\nTruck 2 route:")
    for package in truck2:
        print(package)

    print("\nTruck 3 route:")
    for package in truck3:
        print(package)

# Entry point
if __name__ == '__main__':
    main()
