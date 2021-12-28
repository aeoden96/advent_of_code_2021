def get_input(path):
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            line = list(line.rstrip())
            yield [int(i) for i in line]


height_map = list(get_input("input.txt"))

for i in range(len(height_map)):
    height_map[i] = [9, *height_map[i], 9]

height_map = [[9] * len(height_map[0]), *height_map, [9] * len(height_map[0])]


# [print(i) for i in height_map]

def calc_low(i, j, hm):
    if hm[i - 1][j] > hm[i][j] and hm[i + 1][j] > hm[i][j] and hm[i][j - 1] > hm[i][j] and hm[i][j + 1] > hm[i][j]:
        return True


basins = []
S = 0
for i in range(len(height_map) - 1):
    for j in range(len(height_map[0]) - 1):
        if calc_low(i + 1, j + 1, height_map):
            new_set = set()
            new_set.add((i + 1, j + 1))
            basins.append(new_set)
            S += 1 + height_map[i + 1][j + 1]

# print(S)


for k in range(10):
    for basin_n, basin in enumerate(basins):
        new_places = set()
        for i, j in basin:
            if height_map[i + 1][j] != 9:
                new_places.add((i + 1, j))
            if height_map[i - 1][j] != 9:
                new_places.add((i - 1, j))
            if height_map[i][j + 1] != 9:
                new_places.add((i, j + 1))
            if height_map[i][j - 1] != 9:
                new_places.add((i, j - 1))
        basins[basin_n] = set.union(basins[basin_n], new_places)

import math

basin_lens = sorted([len(i) for i in basins])[-3:]
print(basin_lens)
print(math.prod(basin_lens))
