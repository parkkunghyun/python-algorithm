"""
10000 - WEAK
100000 - NORMAL
STRONG

+ - 해주면 될듯?

"""

import sys

input = sys.stdin.readline

N,M = map(int, input().split(" "))


for _ in range(N):
    combat, power = input().strip().split(" ")
    power = int(power)
    cp[power] = combat
