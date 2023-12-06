from utils import *

g = parse_input()
r = []

q = []
for line in g:
    q.append(line.split()[1:])

time = ''
dist = ''

for line in zip(*q):
    t, d = line
    time += t
    dist += d

time = int(time)
dist = int(dist)

mx = time
mn = 0
for i in range(100):
    cur = (mx + mn) // 2
    d = (time-cur)*cur
    if d < dist:
        mx = (cur + mx) // 2
    else:
        mn = (cur + mn) // 2

mx -= 1
r = mx - (time - mx + 1)

print(r)
pyperclip.copy(r)

