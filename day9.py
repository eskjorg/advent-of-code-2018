import numpy as np
from collections import deque

# Constants
NUM_PLAYERS = 455
LAST_MARBLE = 71223 * 100

# Variables
scores = np.zeros(NUM_PLAYERS)
circle = deque([0])
current_player = 0

for marble in range(1, LAST_MARBLE + 1):
	if marble % 23:
		circle.rotate(-2)
		circle.appendleft(marble)
	else:
		circle.rotate(7)
		scores[current_player] += marble + circle.popleft()
	current_player = (current_player + 1) % NUM_PLAYERS

print(int(max(scores)))