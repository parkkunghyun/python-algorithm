""" 
nn
00칸
상하좌우 가는데 최대한 적게 잃기

00에서 시작함
bfs dfs로 푸는게 나을라나?

"""

import sys
from collections import deque

input = sys.stdin.readline

dy = [0,0,1,-1]
dx = [-1,1,0,0]


def bfs(arr,visited, N):
    que = deque()
    que.append((0,0))
    visited[0][0] = arr[0][0]
    while que:
        y,x = que.popleft()
        for i in range(4):
            cy = dy[i] + y
            cx = dx[i] + x
            if 0 <= cy < N and 0 <= cx < N:
                if visited[cy][cx] > visited[y][x] + arr[cy][cx]:
                    visited[cy][cx] = visited[y][x] + arr[cy][cx]
                    que.append((cy,cx))
    return visited[N-1][N-1]

check = 1

while True:
    N = int(input())
    if N == 0:
        break
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split(" "))))

    visited = [[float('inf') for _ in range(N)] for _ in range(N)]
    ans = bfs(arr,visited, N)
    print(f"Problem {check}: {ans}")
    check += 1