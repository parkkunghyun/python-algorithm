"""
점프

NN
오른쪽 아래
0이 종착지
경로 개수 구하기

백트래킹?
dp라고 들었는데

그 전부 해보고 0인데 나오면 +1하기?

아래로 끝까지 가거나 오른쪽으로 끝까지 가면 안됨!
그냥 0인 부분을 만나면 바로 끝내기!

새로운 방식
1. 배열을 만들어서 내가 갈 수 있는 부분만 체크해두기
2. dp[i][j] > 0 and arr[i][j] > 0 일때만 우축 점프 혹은 아래 점프 하기
3. 
"""

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split(" "))))

result = 0

# def dfs(sy,sx, visited):
#     global result
#     if (arr[sy][sx] == 0):
#         result += 1
#         return
#     if visited[sy][sx] != 1:
#         dy = sy + arr[sy][sx]
#         if ( 0 <= dy and dy < N):
#             dfs(dy, sx)
#         dx = sx + arr[sy][sx]
#         if ( 0 <= dx and dx < N):
#             dfs(sy, dx)

# dfs(0,0)
# visited = [[0 for _ in range(N)] for _ in range(N)]
# print(result, visited)

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if dp[i][j] > 0 and arr[i][j] > 0:
            jump = arr[i][j]
            if j + jump < N:
                dp[i][                                                                                                                                                                                                                                                                                                                                                                                              j+jump] += dp[i][j]
            if i + jump < N:
                dp[i + jump][j] += dp[i][j]

print(dp[N-1][N-1])

for i in range(N):
    for j in range(N):
        print(dp[i][j], end=" ")
    print()
