import os
import re
import numpy as np

with open('data/input03.txt', 'r') as f:
    DATA_INT = [list(map(int, re.findall(r'\d+', line)))
                for line in f.readlines()]
    DATA_NP = np.array(DATA_INT)

max_w = max(DATA_NP[:,1] + DATA_NP[:,3])
max_h = max(DATA_NP[:,2] + DATA_NP[:,4])
fabric = np.zeros((max_h, max_w))

for _, x1, y1, w, h in DATA_NP:
	fabric[y1: y1+h, x1: x1+w] += 1

print("Part 1: ", (fabric > 1).sum())

for patch_id, x1, y1, w, h in DATA_NP:
	if fabric[y1: y1+h, x1: x1+w].sum() == w*h:
		good_patch = patch_id

print("Part 2: ", good_patch)
