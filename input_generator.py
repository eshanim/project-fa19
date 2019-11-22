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


def validate_input(input_file, params=[]):
    message, error = tests(input_file, params)
    return error


def generate_adjacency(num_locations):
    adjacency = [["x" for i in range(num_of_locations)] for j in range(num_of_locations)]

    for i in range(len(adjacency)):
        for j in range(len(adjacency)):
            if j != i:
                randy = round(random.uniform(.1, 20), 5)
                adjacency[i][j] = randy
                adjacency[j][i] = randy

    return adjacency



def generate_locs(num_locations):
    locs = []
    for i in range(num_of_locations):
        locs.append("L" + str(i) + " ")
    print(locs)
    return locs


def generate_start_point(locations):
    return random.choice(locs)


def generate_homes(num_tas, locs):
    homes = []
    count = num_of_tas
    while (count > 0):
        home = random.choice(locs)
        if home not in homes:
            homes.append(home)
            count -= 1
    return homes



# Generating an input of size 30 to 50

num_of_locations = random.randrange(30, 50)
num_of_tas = random.randrange(10, 25)

adjacency = generate_adjacency(num_of_locations)

locs = generate_locs(num_of_locations)

start_point = generate_start_point(locs)

homes = generate_homes(num_of_tas, locs)

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

#Generating an input of size 70 to 100

num_of_locations = random.randrange(70, 100)
num_of_tas = random.randrange(30, 50)

adjacency = generate_adjacency(num_of_locations)

locs = generate_locs(num_of_locations)

start_point = generate_start_point(locs)

homes = generate_homes(num_of_tas, locs)

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


g = "100.in"
write_to_file(g, str(num_of_locations))
write_to_file(g, "\n", True)
write_to_file(g, str(num_of_tas), True)
write_to_file(g, "\n", True)
write_to_file(g, str_loc.join(locs), True)
write_to_file(g, "\n", True)
write_to_file(g, str_loc.join(homes), True)
write_to_file(g, "\n", True)
write_to_file(g, start_point, True)
write_to_file(g, "\n", True)
for list in adjacency:
    write_data_to_file(g, list, " ", True)
    write_to_file(g, "\n", True)


for i in range(random.randint(num_of_locations, (num_of_locations*num_of_locations)-(2*num_of_locations))):
    randi = random.randint(0, num_of_locations - 1)
    randj = random.randint(0, num_of_locations - 1)
    stored = adjacency[randi][randj]
    adjacency[randi][randj] = "x"
    adjacency[randj][randi] = "x"
    write_to_file(g, str(num_of_locations))
    write_to_file(g, "\n", True)
    write_to_file(g, str(num_of_tas), True)
    write_to_file(g, "\n", True)
    write_to_file(g, str_loc.join(locs), True)
    write_to_file(g, "\n", True)
    write_to_file(g, str_loc.join(homes), True)
    write_to_file(g, "\n", True)
    write_to_file(g, start_point, True)
    write_to_file(g, "\n", True)
    for l in adjacency:
        write_data_to_file(g, l, " ", True)
        write_to_file(g, "\n", True)
    if validate_input(g):
        adjacency[randi][randj] = stored
        adjacency[randj][randi] = stored

#Generating an input of size 150 to 200

num_of_locations = random.randrange(150, 200)
num_of_tas = random.randrange(70, 100)

adjacency = generate_adjacency(num_of_locations)

locs = generate_locs(num_of_locations)

start_point = generate_start_point(locs)

homes = generate_homes(num_of_tas, locs)

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


h = "200.in"
write_to_file(h, str(num_of_locations))
write_to_file(h, "\n", True)
write_to_file(h, str(num_of_tas), True)
write_to_file(h, "\n", True)
write_to_file(h, str_loc.join(locs), True)
write_to_file(h, "\n", True)
write_to_file(h, str_loc.join(homes), True)
write_to_file(h, "\n", True)
write_to_file(h, start_point, True)
write_to_file(h, "\n", True)
for list in adjacency:
    write_data_to_file(h, list, " ", True)
    write_to_file(h, "\n", True)


for i in range(random.randint(num_of_locations, (num_of_locations*num_of_locations)-(2*num_of_locations))):
    randi = random.randint(0, num_of_locations - 1)
    randj = random.randint(0, num_of_locations - 1)
    stored = adjacency[randi][randj]
    adjacency[randi][randj] = "x"
    adjacency[randj][randi] = "x"
    write_to_file(h, str(num_of_locations))
    write_to_file(h, "\n", True)
    write_to_file(h, str(num_of_tas), True)
    write_to_file(h, "\n", True)
    write_to_file(h, str_loc.join(locs), True)
    write_to_file(h, "\n", True)
    write_to_file(h, str_loc.join(homes), True)
    write_to_file(h, "\n", True)
    write_to_file(h, start_point, True)
    write_to_file(h, "\n", True)
    for l in adjacency:
        write_data_to_file(h, l, " ", True)
        write_to_file(h, "\n", True)
    if validate_input(h):
        adjacency[randi][randj] = stored
        adjacency[randj][randi] = stored
