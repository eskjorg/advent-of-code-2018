import numpy as np

with open('data/input08.txt', 'r') as f:
    DATA_STR = f.readline().split(" ")
    DATA_INT = list(map(int, DATA_STR))

class Node:
    def __init__(self, n_children, metadata, parent=None):
        self.n_children = n_children
        self.children = []
        self.metadata = metadata
        if parent:
            self.parent = parent
            parent.children.append(self)

    def is_complete(self):
        return self.n_children == len(self.children)

    def sum_recursive(self):
        sum_children = [child.sum_recursive() for child in self.children]
        return sum(self.metadata) + sum(sum_children) 

    def value(self):
        if len(self.children) == 0:
            return sum(self.metadata)
        value = 0
        for metadata in self.metadata:
            if metadata <= len(self.children):
                value += self.children[metadata - 1].value()
        return value

root = current = Node(n_children=1, metadata=[0])

idx = 0
while idx < len(DATA_INT):
    if current.is_complete():
        n_metadata = current.metadata
        current.metadata = DATA_INT[idx: idx + n_metadata]
        current = current.parent
        idx += n_metadata
    else:
        current = Node(*DATA_INT[idx: idx + 2], parent=current)
        idx += 2

print("Part 1: ", root.sum_recursive())
print("Part 2: ", root.value())
