from utils import *

g = parse_input()
r = 0
d = []
locations = []
ranges = []

seeds = parse_nums(' '.join(g[0]))
for dest, rang in zip(seeds[::2], seeds[1::2]):
    ranges.append((dest, dest+rang))


for ind, group in enumerate(g[1:]):
    group = ' '.join(group)
    nums = parse_nums(group)
    d.append([])
    for dest, source, rang in zip(nums[::3], nums[1::3], nums[2::3]):
        d[ind].append((dest, source, rang))

# d.pop()
# d.pop()
# d.pop()
# print()
print('ranges')
for i in ranges:
    print(i)

# print()

# for i in d:
#     print(i)

def getLocation(num):
    for group in d:
        n = num
        for line in group:
            dest, source, rang = line

            if n >= source and n <= source + rang - 1:
                num = dest + (n - source)
    return num

# assert getLocation(79) == 82
# assert getLocation(14) == 43
# assert getLocation(55) == 86
# assert getLocation(13) == 35
# assert getLocation(82) == 46

while ranges:
    rang = ranges.pop()
    # print()
    # print(ranges)
    a, b = rang
    loc = getLocation(a)
    loc2 = getLocation(b)
    locations.append(loc)
    if a == b:
        continue
    locations.append(loc2)
    if b-a == 1:
        continue

    # print(a, b)

    if a-b == loc-loc2:
        # print('YES', a, b, loc, loc2)
        continue
    else:
        # print(a,b)
        mid = (a+b)//2
        # print('mid', mid)
        ranges.append((a, mid))
        ranges.append((mid, b))
# print('locations', locations)

r = min(locations)


print(r)
pyperclip.copy(r)