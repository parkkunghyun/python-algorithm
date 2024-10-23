import sys
from collections import deque

input = sys.stdin.readline

sy = [0, 1, 1, 1]
sx = [1, -1, 0, 1]

def bfs(arr, visited, N):
    que = deque()
    que.append([0,1])
    visited[0][1] = arr[0][1]
    while que:
        y, x = que.popleft()
        for i in range(4):
            cy = sy[i] + y
            cx = sx[i] + x
            if 0<= cy < N and 0<= cx < 3:
                if visited[cy][cx] == 9999:
                    visited[cy][cx] = min(visited[cy][cx], arr[cy][cx] + visited[y][x])
                    que.append([cy,cx])

        print(que, visited)
    return visited[N-1][1]

t = 1
while True:
    res = 1e9
    N = int(input())
    if N == 0:
        break
    arr = []
    visited = [[9999] * 3 for _ in range(N)]
    for _ in range(N):
        arr.append(list(map(int, input().split(" "))))
    res = bfs(arr,visited, N)
    print(f'{t}. {res}')