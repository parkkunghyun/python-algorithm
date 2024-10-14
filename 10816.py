"""
N M

"""

import sys

input = sys.stdin.readline

l = [0 for _ in range(20000001)]

n = int(input())
nList = list(map(int, input().split(" ")))

m = int(input())
mList = list(map(int, input().split(" ")))

for nk in nList:
    nk += 10000000
    l[nk] += 1


for mk in mList:
    mk += 10000000
    print(l[mk], end=" ")
