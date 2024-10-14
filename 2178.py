"""
인접해야하고 1만 가능!
"""
import sys
from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

N,M = map(int, input().split(" "))
arr = []
for _ in range(N):
    l = list(map(int, input()))
    arr.append(l)


visited = [[0 for _ in range(M)] for _ in range(N)]

def bfs():
    que = deque()
    que.append((0,0))
    while que:
        y,x = que.popleft()
        for i in range(4):
            sy = y + dy[i]
            sx = x + dx[i]
            if (0 <= sy < N) and (0 <= sx < M):
                if visited[sy][sx] == 0 and arr[sy][sx] == 1:
                    visited[sy][sx] += visited[y][x] + 1
                    que.append((sy,sx))
visited[0][0] = 0
bfs()
print(visited[N-1][M-1] + 1)