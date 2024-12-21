"""
Equilateral
Isosceles - ab c bc a ac b
Scalene
    Invalid -> 6 32
"""

import sys

input = sys.stdin.readline

while True:
    a,b,c = map(int, input().split(" "))
    if a == 0 and b == 0 and c == 0:
        break
    if a == b and b == c:
        print("Equilateral")
    elif (a==b and a != c) or (a==c and a != b) or (b==c and a != b):
        if a >= b+c or b >= a+c or c >= b+a:
            print("Invalid")
        else:
            print("Isosceles")
    elif a != b and b != c:
        if (a >= b+c) or (b >= a+c) or (c >= b+a):
            print("Invalid")
        else:
            print("Scalene")