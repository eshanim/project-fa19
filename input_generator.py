import random
from utils import *
import sys
sys.path.append('..')
sys.path.append('../..')
import os
import argparse
import utils
import networkx as nx
import numpy as np
from student_utils import *
from input_validator import *

num_of_locations = random.randrange(30, 50)
num_of_tas = random.randrange(10, 25)

def validate_input(input_file, params=[]):
    message, error = tests(input_file, params)
    return error

adjacency = [["x" for i in range(num_of_locations)] for j in range(num_of_locations)]

for i in range(len(adjacency)):
    for j in range(len(adjacency)):
        if j != i:
            randy = round(random.uniform(.1, 20), 5)
            adjacency[i][j] = randy
            adjacency[j][i] = randy

locs = []
for i in range(num_of_locations):
    locs.append("L" + str(i) + " ")
print(locs)
start_point = random.choice(locs)

homes = []
count = num_of_tas
while (count > 0):
    home = random.choice(locs)
    if home not in homes:
        homes.append(home)
        count -= 1

str_loc = ""
str_home = ""


G, m= adjacency_matrix_to_graph(adjacency)


shortest = dict(nx.floyd_warshall(G))
for u, v, datadict in G.edges(data=True):
    if abs(shortest[u][v] - datadict['weight']) >= 0.00001:
        i = u
        j = v
        adjacency[i][j] = round(shortest[u][v], 5)
        adjacency[j][i] = round(shortest[u][v], 5)


f = "50.in"
write_to_file(f, str(num_of_locations))
write_to_file(f, "\n", True)
write_to_file(f, str(num_of_tas), True)
write_to_file(f, "\n", True)
write_to_file(f, str_loc.join(locs), True)
write_to_file(f, "\n", True)
write_to_file(f, str_loc.join(homes), True)
write_to_file(f, "\n", True)
write_to_file(f, start_point, True)
write_to_file(f, "\n", True)
for list in adjacency:
    write_data_to_file(f, list, " ", True)
    write_to_file(f, "\n", True)



for i in range(random.randint(num_of_locations, (num_of_locations*num_of_locations)-(2*num_of_locations))):
    randi = random.randint(0, num_of_locations - 1)
    randj = random.randint(0, num_of_locations - 1)
    stored = adjacency[randi][randj]
    adjacency[randi][randj] = "x"
    adjacency[randj][randi] = "x"
    write_to_file(f, str(num_of_locations))
    write_to_file(f, "\n", True)
    write_to_file(f, str(num_of_tas), True)
    write_to_file(f, "\n", True)
    write_to_file(f, str_loc.join(locs), True)
    write_to_file(f, "\n", True)
    write_to_file(f, str_loc.join(homes), True)
    write_to_file(f, "\n", True)
    write_to_file(f, start_point, True)
    write_to_file(f, "\n", True)
    for l in adjacency:
        write_data_to_file(f, l, " ", True)
        write_to_file(f, "\n", True)
    if validate_input(f):
        adjacency[randi][randj] = stored
        adjacency[randj][randi] = stored
