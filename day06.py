import numpy as np

with open('data/input06.txt', 'r') as f:
    DATA_INT = [list(map(int, line.rstrip().split(",")))
                for line in f.readlines()]
    DATA_NP = np.array(DATA_INT)

height, width = DATA_NP.max(axis=0) - DATA_NP.min(axis=0)
cell_sizes = np.zeros(len(DATA_NP), dtype=int)

for i, j in np.ndindex(height, width):
    distances = np.linalg.norm(DATA_NP - (i, j), ord=1, axis=1)

    idx = np.argmin(distances)
    if i == 0 or i == height - 1 or j == 0 or j == width - 1:
        cell_sizes[idx] = - height * width
    elif (distances == distances[idx]).sum() == 1:
        cell_sizes[idx] += 1

print("Part 1: ", max(cell_sizes))

MARGIN = int(max(height, width) / 2)
sum_dist_grid = np.zeros((MARGIN + height + MARGIN,
                          MARGIN + width + MARGIN))
for coord in np.ndindex(sum_dist_grid.shape):
    distances = np.linalg.norm(DATA_NP + MARGIN - coord, ord=1, axis=1)
    sum_dist_grid[coord] = sum(distances)

print("Part 2: ", (sum_dist_grid < 10000).sum())
