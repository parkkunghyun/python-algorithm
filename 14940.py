import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split(" "))

l = []
for _ in range(N):
    line = list(map(int, input().split(" ")))
    l.append(line)

visited = [[-1 for _ in range(M)] for _ in range(N)]

dy, dx = [1,-1,0,0], [0,0,1,-1]

def bfs(y,x):
    que = deque()
    que.append((y,x))
    visited[y][x] = 0 # 시작 위치!
    while que:
        y,x = que.popleft()
        for i in range(4):
            sy,sx = y + dy[i] , x + dx[i]
            if (0<= sy < N) and (0<= sx < M):
                if visited[sy][sx] == -1 and l[sy][sx] == 1:
                    que.append((sy,sx))
                    visited[sy][sx] = visited[y][x] + 1

for i in range(N):
    for j in range(M):
        if l[i][j] == 2 and visited[i][j] == -1:
            bfs(0,0)
            break

for i in range(N):
    for j in range(M):
        if visited[i][j] == -1:
            print(0, end=" ")
        else:
            print(visited[i][j], end=" ")
    print()