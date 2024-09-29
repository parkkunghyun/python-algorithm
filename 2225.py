"""
0-N -> K == N
순서 상관있음, 모든 경우의 수

permutations -> a,b,c =? 3*2*1
combinations -> a,b,c =?  순서 상관안함
product -> 중복 그리고 순서 고려
combinations_with_replacement -> 중복 순서 고려 안함

일단 정수 k개의 조합을 전부 구하기 -> 그리고 계산하기?
20 2
1 1
0 2
2 0
일단 product는 시간 초과 뜸

k = 1
    n이 무엇이든 무조건 1임
k = 2 -> 1 ~ ....n+1임
    n = 0 -> 0,0 - 1
    n = 1 -> 0,1 - 2
    n = 2 -> 0,2 1,1 - 3
    n = 3 -> 0,3 1,2 - 4
    n = 4 -> 04 40 13 31 22 - 5
    n = 5 -> 05 14 23 32 41 50 - 6
k = 3
    n = 0 000 - 1
    n = 1 001 010 100 - 3
    n = 2 011 002 - 6
    n = 3 003 012 111 - 10
    
k = 4
    n = 0 0000 - 1
    n = 1 0001 - 4
    n = 2 0011 0002 -  10

1
01
001 원래 있던거에 개수만 늘어남!

0 -> 01 -> 뒤에 1추가

n은 같은데 k가 -1이면 0을 추가!

02
11
20

"""
import sys
# from itertools import product

input = sys.stdin.readline

N, K = map(int, input().split(" "))

l = [[0 for _ in range(N+1)] for _ in range(K+1) ]
# data = list(product(l, repeat=K))

# n 과 k로 list를 만들기!
for i in range(1,K+1):
    for j in range(N+1):
        if i == 1:
            l[i][j] = 1
# 
for i in range(1, K+1):
    for j in range(N+1):
        l[i][j] = l[i-1][j] + l[i][j-1]
print(l[K][N] % 1000000000)

"""
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21

"""
    