from utils import *

g = parse_input()
r = 0

for i in g:
    i = parse_nums(i)
    r += int(str(i[0]) + str(i[-1]))

print(r)
pyperclip.copy(r)