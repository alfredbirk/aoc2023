from utils import *

g = parse_input()
r = 0
q = []
c = Counter()

for line in g:
    q.append(line)

for indY ,y in enumerate(q):
    stars = []
    d = ''
    for indX, x in enumerate(y):
        if x.isdigit():
            d += x
        
            for dx, dy in DIRS_8_DELTA:
                px = dx + indX
                py = dy + indY
                if px >= 0 and py >= 0 and px < len(y) and py < len(q) and q[py][px] == '*' and (px, py) not in stars:
                    stars.append((px, py))
            
        else:
            if d != '':
                for px, py in stars:
                    if (px, py) in c:
                        c[(px, py)].append(int(d))
                    else:
                        c[(px, py)] = [int(d)]
            d = ''        
            stars = []


    if d != '':
        for px, py in stars:
            if (px, py) in c:
                c[(px, py)].append(int(d))
            else:
                c[(px, py)] = [int(d)]
    d = ''        
    stars = []


for cords, nums in c.most_common():
    if len(nums) == 2:
        r += math.prod(nums)

print(r)
pyperclip.copy(r)