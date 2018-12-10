import numpy as np

with open('data/input04.txt', 'r') as f:
    DATA_ENTRIES = [line.rstrip() for line in f.readlines()]
DATA_ENTRIES = sorted(DATA_ENTRIES)

def get_id(entry):
    return int(entry.split()[3][1:]) if entry[19] == 'G' else 0
def get_time(entry):
    return int(entry[15:17])

sleep_log = np.zeros((max(map(get_id, DATA_ENTRIES)), 60))
guard_idx = 0
sleep_time = 0

for entry in DATA_ENTRIES:
    indicator = entry[19]
    if indicator == 'G':    # New guard
       guard_idx = get_id(entry) - 1
    elif indicator == 'f':  # Falling asleep
       sleep_time = get_time(entry)
    elif indicator == 'w':  # Waking up
       sleep_log[guard_idx, sleep_time:get_time(entry)] += 1

max_guard_idx = np.argmax(sleep_log.sum(axis=1))
max_guard_max_minute = np.argmax(sleep_log[max_guard_idx,:])
print("Part 1: ", (max_guard_idx + 1) * max_guard_max_minute)

max_guard_idx, max_minute = divmod(np.argmax(sleep_log), 60)
print("Part 2: ", (max_guard_idx + 1) * max_minute)
