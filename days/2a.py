from utils import *

g = parse_input()
r = 0

d = { 'red': 12, 'green': 13, 'blue': 14}

for line in g:
    _, nr, *a = line.split()
    good = True
    for num, col in zip(a[::2], a[1::2]):
        if col[-1] == ',' or col[-1] == ';':
            col = col[:-1]
        num = int(num)
    
        if d[col] < num:
            good = False
    if good == True:
        r += int(nr[:-1])



print(r)
pyperclip.copy(r)