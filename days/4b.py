from utils import *

g = parse_input()
r = 0

c = Counter()
stack = []
d = {}
total = 0
q = []

for i in range(len(g)):
    stack.append(i)

for ind, line in enumerate(g):
    a, b = line.split('|')
    a = parse_nums(a.split(':')[1:][0])
    b = parse_nums(b)
    q.append((a,b))
while stack:
    cur_index = stack.pop()
    cur = q[cur_index]
    a, b = cur
    total += 1
    matches = len([i for i in a if i in b])
    summ = 1
    for i in range(matches):
        if cur_index + i < len(q):
            summ += d[cur_index + i + 1]
    d[cur_index] = summ

r = sum(d.values())

print(r)
pyperclip.copy(r)