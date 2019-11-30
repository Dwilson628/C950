import csv


# chaining hash table
class ListHash:

    # initializes the table with a default of 10 buckets
    def __init__(self, length=10):

        # assigns each bucket an empty list
        self.table = []
        for i in range(length):
            self.table.append([])

    def insert(self, key, package):

        # this function uses the first index (package ID) as a key
        # and inserts the entire list into the bucket
        package[0] = int(package[0])
        bucket = key % len(self.table)
        self.table[bucket].append(package)
        package.append('At Hub')

    def search(self, key):

        # finds bucket just like insert function
        bucket = key % len(self.table)
        bucket_list = self.table[bucket]

        # once bucket is found, searches bucket for given key
        for package in bucket_list:
            if package[0] == key:
                return package

        # returns 0 if package isn't found
        return 0

    def remove(self, key):

        # finds bucket and package just like search
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # if package is found, removes package
        # does nothing otherwise
        for package in bucket_list:
            if package[0] == key:
                bucket_list.remove(package)


def get_packages(filename):

    # creates a hash table based off of csv file data
    new_hash = ListHash()
    with open(filename) as csvDataFile:

        csv_reader = csv.reader(csvDataFile)

        # each line in the csv is a complete formatted package
        # inserts entire row into the hash table with row[0] being package ID
        for row in csv_reader:
            new_hash.insert(int(row[0]), row)
    return new_hash


# calls function to make the table using our csv
hashtable = get_packages('WGUPS Package File.csv')
