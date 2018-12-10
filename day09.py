import os
import numpy as np
from collections import deque

with open('data/input9.txt', 'r') as f:
    line = f.readline().split(" ")
    NUM_PLAYERS = int(line[0])
    LAST_MARBLE = int(line[6])

def play(num_marbles):
	scores = np.zeros(NUM_PLAYERS)
	circle = deque([0])
	current_player = 0
	
	for marble in range(1, num_marbles + 1):
		if marble % 23:
			circle.rotate(-2)
			circle.appendleft(marble)
		else:
			circle.rotate(7)
			scores[current_player] += marble + circle.popleft()
		current_player = (current_player + 1) % NUM_PLAYERS
	return int(max(scores))

print("Part 1: ", play(LAST_MARBLE))
print("Part 2: ", play(LAST_MARBLE * 100))
