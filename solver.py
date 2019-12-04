import os
import sys
sys.path.append('..')
sys.path.append('../..')
import argparse
import utils
import networkx as nx
import student_utils

import matplotlib.pyplot as plt

from student_utils import *
"""
======================================================================
  Complete the following function.
======================================================================
"""

def solve(list_of_locations, list_of_homes, starting_car_location, adjacency_matrix, params=[]):
    """
    Write your algorithm here.
    Input:
        list_of_locations: A list of locations such that node i of the graph corresponds to name at index i of the list
        list_of_homes: A list of homes
        starting_car_location: The name of the starting location for the car
        adjacency_matrix: The adjacency matrix from the input file
    Output:
        A list of locations representing the car path
        A dictionary mapping drop-off location to a list of homes of TAs that got off at that particular location
        NOTE: both outputs should be in terms of indices not the names of the locations themselves
    """




    path = [starting_car_location]
    dict = {}
    index = 0
    for i in range(len(list_of_locations)):
        if list_of_locations[i] == starting_car_location:
            index = i

    path = [index]

    G, m = adjacency_matrix_to_graph(adjacency_matrix)


    home_indexes = []

    for home in list_of_homes:
        for i in range(len(list_of_locations)):
            if list_of_locations[i] == home:
                home_indexes.append(i)
                break

    new_adjacency = [["x" for i in range(len(list_of_locations))] for j in range(len(list_of_locations))]

    # for sake of figuring out where to walk
    for home in home_indexes:
        di_path = nx.dijkstra_path(G, index, home)
        for i in range(len(di_path) -  1):
            new_adjacency[di_path[i]][di_path[i + 1]] = adjacency_matrix[di_path[i]][di_path[i + 1]]
            new_adjacency[di_path[i + 1]][di_path[i]] = adjacency_matrix[di_path[i]][di_path[i + 1]]


    for home1 in home_indexes:
        for home2 in home_indexes:
            if not home1 == home2:
                di_path = nx.dijkstra_path(G, home1, home2)
                for i in range(len(di_path) -  1):
                    new_adjacency[di_path[i]][di_path[i + 1]] = adjacency_matrix[di_path[i]][di_path[i + 1]]
                    new_adjacency[di_path[i + 1]][di_path[i]] = adjacency_matrix[di_path[i]][di_path[i + 1]]




    G2, m = adjacency_matrix_to_graph(new_adjacency)

    all_driving_path = list(nx.dfs_edges(G2))




    walking_to = []
    walking_from = {}


    for i in range(len(new_adjacency)):
        if i in home_indexes:
            count = 0
            edge_to = 0
            for j in range(len(new_adjacency)):
                if new_adjacency[i][j] != "x":
                    count += 1
                    edge_to = j

            if count == 1:
                new_adjacency[i][edge_to] = "x"
                new_adjacency[edge_to][i] = "x"
                walking_to.append(i)
                if edge_to in walking_from:
                    walking_from[edge_to] = walking_from[edge_to] + [i]
                else:
                    walking_from[edge_to] = [i]

    #
    # for i in range(len(all_driving_path) - 1):
    #     #if first vertex in edge is the same, we should walk
    #     if all_driving_path[i][0] == all_driving_path[i + 1][0]:
    #         print(all_driving_path[i][0])
    #         print(all_driving_path[i][1])
    #         #get rid of only edge connected to this home
    #         new_adjacency[all_driving_path[i][0]][all_driving_path[i][1]] = "x"
    #         new_adjacency[all_driving_path[i][1]][all_driving_path[i][0]] = "x"
    #         walking_to.append(all_driving_path[i][1])
    #         if all_driving_path[i][0] in walking_from:
    #             walking_from[all_driving_path[i][0]] = walking_from[all_driving_path[i][0]] + [all_driving_path[i][1]]
    #         else:
    #             walking_from[all_driving_path[i][0]] = [all_driving_path[i][1]]



    dropoff_locations = list(walking_from.keys())
    for loc in dropoff_locations:
        if loc in home_indexes:
            dropoff_locations.remove(loc)


    for loc in dropoff_locations:
        di_path = nx.dijkstra_path(G, loc, home)
        for i in range(len(di_path) -  1):
            new_adjacency[di_path[i]][di_path[i + 1]] = adjacency_matrix[di_path[i]][di_path[i + 1]]
            new_adjacency[di_path[i + 1]][di_path[i]] = adjacency_matrix[di_path[i]][di_path[i + 1]]

    for loc in dropoff_locations:
        for home in home_indexes:
            di_path = nx.dijkstra_path(G, loc, home)
            for i in range(len(di_path) -  1):
                new_adjacency[di_path[i]][di_path[i + 1]] = adjacency_matrix[di_path[i]][di_path[i + 1]]
                new_adjacency[di_path[i + 1]][di_path[i]] = adjacency_matrix[di_path[i]][di_path[i + 1]]


    G2, m = adjacency_matrix_to_graph(new_adjacency)

    # condensed shortest paths to edges - use G3 for real

    new_adjacency2 = [["x" for i in range(len(list_of_locations))] for j in range(len(list_of_locations))]

    for home in home_indexes:
        if home not in walking_to:
            di_path = nx.dijkstra_path(G2, index, home)
            start = di_path[0]
            end = di_path[len(di_path) - 1]
            new_adjacency2[start][end] = 0
            new_adjacency2[end][start] = 0
            for i in range(len(di_path) -  1):
                new_adjacency2[start][end] += new_adjacency[di_path[i]][di_path[i + 1]]
                new_adjacency2[end][start] += new_adjacency[di_path[i]][di_path[i + 1]]


    for home1 in home_indexes:
        for home2 in home_indexes:
            if not home1 == home2 and home1 not in walking_to and home2 not in walking_to:
                di_path = nx.dijkstra_path(G2, home1, home2)
                start = di_path[0]
                end = di_path[len(di_path) - 1]
                new_adjacency2[start][end] = 0
                new_adjacency2[end][start] = 0
                for i in range(len(di_path) -  1):
                    new_adjacency2[start][end] += new_adjacency[di_path[i]][di_path[i + 1]]
                    new_adjacency2[end][start] += new_adjacency[di_path[i]][di_path[i + 1]]

    for loc in dropoff_locations:
        di_path = nx.dijkstra_path(G2, index, loc)
        start = di_path[0]
        end = di_path[len(di_path) - 1]
        new_adjacency2[start][end] = 0
        new_adjacency2[end][start] = 0
        for i in range(len(di_path) -  1):
            new_adjacency2[start][end] += new_adjacency[di_path[i]][di_path[i + 1]]
            new_adjacency2[end][start] += new_adjacency[di_path[i]][di_path[i + 1]]

    for loc in dropoff_locations:
        for home in home_indexes:
            di_path = nx.dijkstra_path(G2, loc, home)
            start = di_path[0]
            end = di_path[len(di_path) - 1]
            new_adjacency2[start][end] = 0
            new_adjacency2[end][start] = 0
            for i in range(len(di_path) -  1):
                new_adjacency2[start][end] += new_adjacency[di_path[i]][di_path[i + 1]]
                new_adjacency2[end][start] += new_adjacency[di_path[i]][di_path[i + 1]]




    final_G, m = adjacency_matrix_to_graph(new_adjacency2)
    drive_path = list(nx.dfs_edges(final_G, source=index))
    drive_path.append(index)

    mst = nx.minimum_spanning_tree(final_G)
    path = list(nx.dfs_preorder_nodes(mst, index))
    # print(path)
    final_path = []
    for node in path:
        if node == index:
            final_path.append(node)
            # print("Index: ", node)
        elif node in home_indexes and node not in walking_to:
            final_path.append(node)
            # print("Home but not walking: ", node)
        elif node in dropoff_locations:
            final_path.append(node)
            # print("Dropoff loc: ", node)
    final_path.append(index)
    print(walking_from)
    # print(final_path)
    # nx.draw(mst)
    # plt.draw()
    # plt.show()

    for node in final_path:
        if node in walking_from:
            dict[node] = walking_from[node]
        elif node in home_indexes:
            dict[node] = [node]

    # print(final_path)
    # print(dict)


    return final_path, dict

    pass

"""
======================================================================
   No need to change any code below this line
======================================================================
"""

"""
Convert solution with path and dropoff_mapping in terms of indices
and write solution output in terms of names to path_to_file + file_number + '.out'
"""
def convertToFile(path, dropoff_mapping, path_to_file, list_locs):
    string = ''
    for node in path:
        string += list_locs[node] + ' '
    string = string.strip()
    string += '\n'

    dropoffNumber = len(dropoff_mapping.keys())
    string += str(dropoffNumber) + '\n'
    for dropoff in dropoff_mapping.keys():
        strDrop = list_locs[dropoff] + ' '
        for node in dropoff_mapping[dropoff]:
            strDrop += list_locs[node] + ' '
        strDrop = strDrop.strip()
        strDrop += '\n'
        string += strDrop
    utils.write_to_file(path_to_file, string)

def solve_from_file(input_file, output_directory, params=[]):
    print('Processing', input_file)

    input_data = utils.read_file(input_file)
    num_of_locations, num_houses, list_locations, list_houses, starting_car_location, adjacency_matrix = data_parser(input_data)
    car_path, drop_offs = solve(list_locations, list_houses, starting_car_location, adjacency_matrix, params=params)

    basename, filename = os.path.split(input_file)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    output_file = utils.input_to_output(input_file, output_directory)
    print(car_path)
    convertToFile(car_path, drop_offs, output_file, list_locations)


def solve_all(input_directory, output_directory, params=[]):
    input_files = utils.get_files_with_extension(input_directory, 'in')

    for input_file in input_files:
        solve_from_file(input_file, output_directory, params=params)


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Parsing arguments')
    parser.add_argument('--all', action='store_true', help='If specified, the solver is run on all files in the input directory. Else, it is run on just the given input file')
    parser.add_argument('input', type=str, help='The path to the input file or directory')
    parser.add_argument('output_directory', type=str, nargs='?', default='.', help='The path to the directory where the output should be written')
    parser.add_argument('params', nargs=argparse.REMAINDER, help='Extra arguments passed in')
    args = parser.parse_args()
    output_directory = args.output_directory
    if args.all:
        input_directory = args.input
        solve_all(input_directory, output_directory, params=args.params)
    else:
        input_file = args.input
        solve_from_file(input_file, output_directory, params=args.params)
