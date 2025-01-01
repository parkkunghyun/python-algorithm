""" 
w h

N M
5 4 1 1
처음부터 그만큼씩 
"""

import sys
import math

input = sys.stdin.readline

H,W,N,M = map(int, input().split(" "))

a = math.ceil(H / (N+1))
b = math.ceil(W / (M+1))
print(a*b)

