import os
import numpy as np

with open('data/input8.txt', 'r') as f:
    DATA_STR = f.readline().split(" ")
    DATA_INT = list(map(int, DATA_STR))

class Node:
	def __init__(self, parent=None, metadata=None):
		if parent:
			self.parent = parent
			parent.childs.append(self)
		self.childs = []
		self.metadata = metadata or []

	def sum_recursive(self):
		sum_childs = [child.sum_recursive() for child in self.childs]
		return sum(self.metadata) + sum(sum_childs) 

	def value(self):
		if len(self.childs) == 0:
			return sum(self.metadata)
		value = 0
		for metadata in self.metadata:
			if metadata <= len(self.childs):
				value += self.childs[metadata - 1].value()
		return value

root = current = Node(metadata=[0])
node_stack = [[1, 0]]  # [c, m] = [n_childs, n_metadata]

idx = 0
while idx < len(DATA_INT):
	if node_stack[-1][0] == 0:  # No more children -> collect metadata
		_, n_metadata = node_stack.pop()
		current.metadata.extend(DATA_INT[idx: idx + n_metadata])
		current = current.parent
		idx += n_metadata
	else:
		node_stack[-1][0] -= 1
		node_stack.append(DATA_INT[idx: idx + 2])
		current = Node(parent=current)
		idx += 2

print("Part 1: ", root.sum_recursive())
print("Part 2: ", root.value())
