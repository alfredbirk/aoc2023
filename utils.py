import re
import math
import operator
from functools import total_ordering, reduce
from math import sqrt, prod
from itertools import count, islice
import typing
import sys

import pyperclip, re, math, itertools, collections, networkx as nx, utils
from string import ascii_uppercase, ascii_lowercase
from collections import Counter, defaultdict, deque
from itertools import (
    product,
    permutations,
    combinations,
    combinations_with_replacement,
    zip_longest,
    cycle,
    groupby
)
from re import findall, fullmatch


LETTERS = [x for x in "abcdefghijklmnopqrstuvwxyz"]
VOWELS = {"a", "e", "i", "o", "u"}
CONSONANTS = set(x for x in LETTERS if x not in VOWELS)


def parse_line(regex, line):
    ret = []
    for match in re.match(regex, line).groups():
        try:
            ret.append(int(match))
        except ValueError:
            ret.append(match)

    return ret


def parse_nums(line, negatives=True):
    num_re = r"-?\d+" if negatives else r"\d+"
    return [int(n) for n in re.findall(num_re, line)]


def parse_positive_nums(line, negatives=False):
    num_re = r"-?\d+" if negatives else r"\d+"
    return [int(n) for n in re.findall(num_re, line)]

def parse_letters(line):
    letter_re = r"[a-zA-Z]+"
    return re.findall(letter_re, line)


def lmap(func, *iterables):
    return list(map(func, *iterables))


def parse_floats(s: str) -> typing.List[float]:
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))


def parse_positive_floats(s: str) -> typing.List[float]:
    return lmap(float, re.findall(r"\d+(?:\.\d+)?", s))

def parse_in_square_brackets(line):
    return re.findall(f"\[(.*?)\]", line)

def parse_in_parenthesis(line):
    return re.findall(f"\((.*?|)\)", line)


def new_grid(val, width, height):
    return [[val for _ in range(width)] for _ in range(height)]


def chunks(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def factors(n):
    """Returns the factors of n."""
    return sorted(
        x
        for tup in ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0)
        for x in tup
    )


def _eratosthenes(n):
    """http://stackoverflow.com/a/3941967/239076"""
    # Initialize list of primes
    _primes = [True] * n

    # Set 0 and 1 to non-prime
    _primes[0] = _primes[1] = False

    for i, is_prime in enumerate(_primes):
        if is_prime:
            yield i

            # Mark factors as non-prime
            for j in range(i * i, n, i):  # NOQA
                _primes[j] = False


def primes(n):
    """Return a list of primes from [2, n)"""
    return list(_eratosthenes(n))


def fibonacci(n):
    """Return a list of fibonacci numbers from [1, n)"""
    f = [1, 1]
    for i in range(n - 2):
        f.append(f[-1] + f[-2])
    return f


DIRS_4_DELTA = [
    (0, 1),  # north
    (1, 0),  # east
    (0, -1),  # south
    (-1, 0),  # west
]

DIRS_8_DELTA = [
    (0, 1),  # N
    (1, 1),  # NE
    (1, 0),  # E
    (1, -1),  # SE
    (0, -1),  # S
    (-1, -1),  # SW
    (-1, 0),  # W
    (-1, 1),  # NW
]

DIRS_DICT = {
    "N": (0, 1),  # north
    "E": (1, 0),  # east
    "S": (0, -1),  # south
    "W": (-1, 0),  # west

    "^": (0, 1),  # north
    ">": (1, 0),  # east
    "v": (0, -1),  # south
    "<": (-1, 0),  # west

    "U": (0, 1),  # north
    "R": (1, 0),  # east
    "D": (0, -1),  # south
    "L": (-1, 0),  # west

    0: (0, 1),  # north
    1: (1, 0),  # east
    2: (0, -1),  # south
    3: (-1, 0),  # west

    "NE": (1, 1),  
    "SE": (1, -1),  
    "SW": (-1, -1),  
    "NW": (-1, 1),  
}

def dirs_4_neighbours(x, y):
    neighbours = []
    for dx, dy in DIRS_4_DELTA:
        nx, ny = x+dx, y+dy
        neighbours.append((nx, ny))
    return neighbours


def walk_dir(x, y, dir):
    dx, dy = DIRS_DICT[dir]
    return (x + dx, y + dy)


def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:  # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:  # these two are the actual lines
                break  # you're looking for
            lower = x
        elif target < val:
            upper = x


def isPrime(n):
    if n < 2:
        return False
    return all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def parse_input(string=False, join=False, raw=False):
    c = 0
    is_multiline = False
    has_double_line_break = False
    is_one_digit_per_line = True
    is_multiple_digits_per_line = True
    digits = 0
    spaces = 0
    total = 0

    with open("inp.txt", "r") as f:
        for line in f:
            line = line.strip()
            num_re = r"-?\+?\d+"
            if is_one_digit_per_line and not fullmatch(num_re, line):
                is_one_digit_per_line = False
            
            if is_multiple_digits_per_line:
                line2 = line.split()
                if len(line2) > 1 and all(i.isdigit() for i in line2):
                    is_multiple_digits_per_line = True
                else:
                    is_multiple_digits_per_line = False

            if line == '':
                has_double_line_break = True
            for i in line:
                if i.isdigit():
                    digits += 1
                elif i == " ":
                    spaces += 1
                total += 1
            c += 1
            if c > 8:
                break

    if c > 1:
        is_multiline = True
    
    g = []
    with open(sys.argv[1], "r") as f:
        if has_double_line_break:
            g = f.read().split('\n\n')
            g2 = []
            if join:
                for line in g:
                    g2.append(line.replace('\n', ''))
            else:
                for line in g:
                    g2.append(line.split())
            return g2

        for line in f:
            line = line.strip()
            if is_one_digit_per_line and not raw:
                if string:
                    g.append(line.strip())
                else:
                    g.append(int(line.strip()))
            elif digits + spaces == total and not raw:
                if string:
                    g.append(line.strip().split())
                else:
                    g.append(list(map(int, line.strip().split())))
            else:
                g.append(line)

        if is_multiline == False:
            g = g[0]
            if is_multiple_digits_per_line:
                g = list(map(int, g.split()))

    return g