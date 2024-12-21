"""
NM
아래로만 가능
같은방향 두번 안됨
연료 최솟값 구하기

반대로 아래서 위로 가기?

1 2 3을 가정하기 -> 이때 3차원배열로?
각 부분에서 시작했다고 가정
5 8 5 1
8 10 9 5
지나온 방식을 저장 - visited
"""

import sys

input = sys.stdin.readline

N,M = map(int, input().split(" "))
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split(" "))))

dp = [[[int(1e9)] * 3 for _ in range(M)] for _ in range(N+1)]

for j in range(M):
    for k in range(3):
        dp[0][j][k] = 0

for i in range(1, N+1):
    for j in range(M):
        if j == 0:
            dp[i][j][1] = dp[i-1][j][2] + arr[i-1][j]
            dp[i][j][2] = min(dp[i-1][j+1][0], dp[i-1][j+1][1]) + arr[i-1][j]
        