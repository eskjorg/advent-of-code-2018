import numpy as np
from PIL import Image

with open('data/input10.txt', 'r') as f:
    DATA_ENTRIES = [line.rstrip() for line in f.readlines()]

entries = np.zeros((len(DATA_ENTRIES),4), dtype=int)
for i, entry in enumerate(DATA_ENTRIES):
    entries[i,0] = entry[10:16]
    entries[i,1] = entry[18:24]
    entries[i,2] = entry[36:38]
    entries[i,3] = entry[40:42]

min_time = -int((entries[:,:2] / entries[:,2:]).max())
max_time = -int((entries[:,:2] / entries[:,2:]).min())

time = min_time + np.argmin([np.std(entries[:,:2] + t * entries[:,2:])
                             for t in range(min_time, max_time)])
coords = entries[:,:2] + time * entries[:,2:]
coords -= coords.min(axis=0) - 1

img = np.zeros(1 + coords.max(axis=0) + 1).T
img[coords[:,1], coords[:,0]] = 255
Image.fromarray(img).resize(10 * np.array(img.shape[::-1])).show()

print("Part 1: ", "...")
print("Part 2: ", time)
