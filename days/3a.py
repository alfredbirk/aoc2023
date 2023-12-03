from utils import *

g = parse_input()
r = 0
q = []

for line in g:
    q.append(line)

for indY ,y in enumerate(q):
    hasSymbol = False
    d = ''
    for indX, x in enumerate(y):
        if x.isdigit():
            d += x
        
            for dx, dy in DIRS_8_DELTA:
                px = dx + indX
                py = dy + indY
                if px >= 0 and py >= 0 and px < len(y) and py < len(q) and not q[py][px].isdigit() and q[py][px] != '.':
                    hasSymbol = True
            
        else:
            if d != '':
                if hasSymbol:
                    print(d)
                    r += int(d)
            d = ''        
            hasSymbol = False

    if d != '':
        if hasSymbol:
            print(d)
            r += int(d)
    d = ''        
    hasSymbol = False


print(r)
pyperclip.copy(r)