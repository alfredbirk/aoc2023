from utils import *

g = parse_input()
r = 0

c = Counter()

for line in g:
    a, b = line.split('|')
    a = parse_nums(a.split(':')[1:][0])
    b = parse_nums(b)
    both = [i for i in a if i in b]
    if len(both) > 0:
        r += 2**(len(both)-1)

print(r)
pyperclip.copy(r)