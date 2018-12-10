import string

with open('data/input05.txt', 'r') as f:
    DATA_STR = f.readline().rstrip()

def react(polymer, unit=''):
    polymer = polymer.replace(unit, '').replace(unit.upper(), '')
    i = 0
    while i < len(polymer) - 1:
        if polymer[i] == polymer[i+1].swapcase():
            polymer = polymer[:i] + polymer[i+2:]
            i = max(0, i - 1)
        else:
            i += 1
    return(len(polymer))

print("Part 1: ", react(DATA_STR))
print("Part 2: ", min(react(DATA_STR, alpha) for alpha in string.ascii_lowercase))
