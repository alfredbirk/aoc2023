from utils import *

g = parse_input()
q = [i.split()[1:] for i in g]
r = []

for line in zip(*q):
    t, d = list(map(int, line))
    cur = 0
    for i in range(t+1):
        dist = (t-i)*i
        if dist >= d:
            cur += 1
    r.append(cur)

r = math.prod(r)
print(r)
pyperclip.copy(r)

