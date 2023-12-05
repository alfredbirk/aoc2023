from utils import *

g = parse_input()
r = 0
d = []
locations = []
ranges = []

seeds = parse_nums(' '.join(g[0]))
for dest, rang in zip(seeds[::2], seeds[1::2]):
    ranges.append((dest, rang))


for ind, group in enumerate(g[1:]):
    group = ' '.join(group)
    nums = parse_nums(group)
    d.append([])
    for dest, source, rang in zip(nums[::3], nums[1::3], nums[2::3]):
        d[ind].append((dest, source, rang))

d.pop()
d.pop()
d.pop()
print()
print('ranges')
for i in ranges:
    print(i)

print()

# for i in d:
#     print(i)

def getLocation(num):
    for group in d:
        for line in group:
            dest, source, rang = line
            if num >= source and num <= source + rang:
                num = dest + (num - source)
                
    return num

while ranges:
    rang = ranges.pop()
    # print('len', len(ranges))
    # print(ranges)
    a, b = rang
    loc = getLocation(a)
    loc2 = getLocation(b)
    locations.append(loc)
    locations.append(loc2)

    # print(a, b)

    if abs(a-b) == abs(loc-loc2):
        # print('YES')
        continue
    else:
        # print(a,b)
        mid = (b-a)//2
        # ranges.append((a, mid))
        # ranges.append((mid, b))
print('locations', locations)

# r = min(locations)


print(r)
pyperclip.copy(r)