from utils import *

g = parse_input()
r = 0

w = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for i in g:
    for ind, word in enumerate(w):
        i = i.replace(word, word + str((ind + 1)) + word)
    
    i = ''.join(map(str, parse_nums(i)))
    r += int(str(i[0]) + str(i[-1]))

print(r)
pyperclip.copy(r)