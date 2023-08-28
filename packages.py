import csv

def load_package_data(csv_filename):
    packages = []
    with open(csv_filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            packages.append(row)
    return packages
