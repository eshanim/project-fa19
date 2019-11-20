import random
num_of_locations = random.randrange(30, 50)
num_of_tas = random.randrange(10, 25)

adjacency = [["x"] * num_of_locations] * num_of_locations

for i in range(length(adjacency)):
	for j in length(i):
		if j != i:
			randy = round(random.uniform(.1, 20), 5)
			adjacency[i][j] = randy
			adjacency[j][i] = randy



