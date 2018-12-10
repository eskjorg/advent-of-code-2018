import os
from itertools import product

with open('data/input02.txt', 'r') as f:
    DATA_STR = [line.rstrip() for line in f.readlines()]

def has_multiple(string, num):
	return any(string.count(char) == num for char in string)

duples = map(lambda x: has_multiple(x, 2), DATA_STR)
triples = map(lambda x: has_multiple(x, 3), DATA_STR)

print("Part 1: ", sum(duples) * sum(triples))

for str_a, str_b in product(DATA_STR, DATA_STR):
	diff = [char_a != char_b for char_a, char_b in zip(str_a, str_b)]
	if sum(diff) == 1:
		idx = diff.index(1)
		common = str_a[:idx] + str_a[idx + 1:]
		break

print("Part 2: ", common)
