"""
잘못되면 0을 출력
A - 1
Z - 26

BEAN -> 25114

암호의 해석이 나올수있는 가지수 구하기!

1000000으로 나눈 나머지 출

25114

a - 1 b - 2 c - 3 d - 4 e - 5 f - 6 g - 7 h - 8 i 9 
j 10 k 11 l 12 m 13 n 14 o 15 p 16 q 17 r 18 s 19
t 20 u - 21 v - 22 w - 23 x - 24 y - 25 z - 26

25114

2 5 1 1 4
25 

일단 2자리씩 붙을 수 있는지 확인

2 5 1 1 1 4
25 11 14
25 1 1 1 4
25 11 1 4
2 5 11 1 4
2 5 1 1 14


"""

import sys

input = sys.stdin.readline

cypher = input().rstrip()


print(ord('s')- 97)