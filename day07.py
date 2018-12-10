import numpy as np
from string import ascii_uppercase as alphabet

NUM_WORKERS = 5
with open('data/input07.txt', 'r') as f:
    DATA_STR = [line.rstrip().split(" ") for line in f.readlines()]

deps = np.zeros((len(alphabet), len(alphabet)))
for line in DATA_STR:
    step = alphabet.find(line[1])
    before = alphabet.find(line[7])
    deps[before, step] = 1
deps_c = np.copy(deps)

# Problem 1

order = ""
for _ in range(len(alphabet)):
    for l, line in enumerate(deps):
        if not any(line):
            order += alphabet[l]
            deps[:,l] = 0
            deps[l,l] = -1
            break

print("Part 1: ", order)

# Problem 2

schedule = np.zeros(((60 + 13) * 26, NUM_WORKERS))
finished = set()
started = set()

def get_task(task_id=-1, task_len=1):
    for letter_id in map(alphabet.index, order):
        if letter_id not in started and not any(deps_c[letter_id]):
            task_id = letter_id + 1
            task_len = 60 + task_id
            started.add(letter_id)
            break
    return task_id, task_len

time = 0
while len(finished) < 26:
    time += 1
    for w in range(NUM_WORKERS):  # Finish tasks
        if schedule[time, w] == 0 and schedule[time-1, w] > 0:
            letter_id = int(round(schedule[time-1, w] - 1))
            finished.add(letter_id)
            deps_c[:, letter_id] = 0
    for w in range(NUM_WORKERS):  # Start tasks
        if schedule[time, w] == 0:
            task_id, task_len = get_task()
            schedule[time: time + task_len, w] = task_id

print("Part 2: ", time - 1)
