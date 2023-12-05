from utils import *

g = parse_input()
r = 0


seeds = parse_nums(' '.join(g[0]))

d = []
locations = []

for ind, group in enumerate(g[1:]):
    group = ' '.join(group)
    nums = parse_nums(group)
    d.append([])
    for dest, source, rang in zip(nums[::3], nums[1::3], nums[2::3]):
        print(dest, source, rang)
        d[ind].append((dest, source, rang))

for seed in seeds:
    for group in d:
        for line in group:
            dest, source, rang = line
            if seed >= source and seed <= source + rang:
                seed = dest + (seed - source)
                break
    locations.append(seed)

r = min(locations)

print(r)
pyperclip.copy(r)