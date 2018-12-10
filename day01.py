import os

with open('data/input1.txt', 'r') as f:
    DATA_STR = f.readlines()
    DATA_INT = list(map(int, DATA_STR))

print("Part 1: ", sum(DATA_INT))

######## ALTERNATIVE 1 ##########
import numpy as np
frequencies = set()

max_cycle = int((max(DATA_INT) - min(DATA_INT)) / sum(DATA_INT))
for frequency in np.cumsum(DATA_INT * max_cycle):
	if frequency in frequencies:
		doublet = frequency
		break
	frequencies.add(frequency)

#print("Part 2: ", doublet)

######## ALTERNATIVE 2 ##########
from itertools import cycle
frequencies = set()

frequency = 0
for delta_f in cycle(DATA_INT):
	frequency += delta_f
	if frequency in frequencies:
		doublet = frequency
		break
	frequencies.add(frequency)

print("Part 2: ", doublet)
