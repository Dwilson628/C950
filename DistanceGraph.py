import csv


class Graph:
    def __init__(self):

        self.address_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):

        # populates the address list dictionary with keys and empty lists
        self.address_list[new_vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight=1.0):

        # logs distance between two addresses
        # would need to split into two functions if distances weren't symmetric
        if from_vertex != to_vertex:
            self.edge_weights[(from_vertex, to_vertex)] = weight

    def populate_address(self, hashtable):

        # Goes through every package and puts it into dictionary with address as key
        # Speeds up loading trucks by address instead of by individual package
        for bucket in hashtable.table:
            for item in bucket:
                self.address_list[item[1]].append(item)


def read_csv(filename):

    # stores csv data into a separate matrix that can be called later instead of reading csv every time
    csv_matrix = []
    with open(filename) as csvDataFile:
        csv_reader = csv.reader(csvDataFile)

        # storing entire row, but indexes 0-2 are address strings
        for row in csv_reader:
            csv_matrix.append(row)
    return csv_matrix


def get_graph(filename):

    matrix = read_csv(filename)
    graph = Graph()

    # read_csv function got matrix with address data at index 1
    # stores that address into our graph
    for row in matrix:
        graph.add_vertex(row[1])

    # populates graph edge weight list using the rest of the distance table
    for row in matrix:
        for i in range(3, len(row)):
            graph.add_edge(row[1], matrix[i-3][1], float(row[i]))

    return graph
