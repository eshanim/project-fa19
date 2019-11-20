import random
from utils import *
num_of_locations = 5 #random.randrange(30, 50)
num_of_tas = 3 #random.randrange(10, 25)

adjacency = [["x"] * num_of_locations] * num_of_locations

for i in range(len(adjacency)):
	for j in range(len(adjacency)):
		if j != i:
			randy = round(random.uniform(.1, 20), 5)
			adjacency[i][j] = randy
			adjacency[j][i] = randy

locs = []
for i in range(num_of_locations):
	locs.append("L" + str(i) + " ")

homes = []
count = num_of_tas
while (count > 0):
	home = random.choice(locs)
	if home not in homes:
		homes.append(home)
		count -= 1

str_loc = ""
str_home = ""

f = "50.in"
write_to_file(f, str(num_of_locations))
write_to_file(f, "\n", True)
write_to_file(f, str(num_of_tas), True)
write_to_file(f, "\n", True)
write_to_file(f, str_loc.join(locs), True)
write_to_file(f, "\n", True)
write_to_file(f, str_loc.join(homes), True)
write_to_file(f, "\n", True)
write_data_to_file(f, adjacency, "\n", True)
