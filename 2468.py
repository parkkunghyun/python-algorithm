import sys
from collections import deque

sy = [-1,1,0,0]
sx = [0,0,-1,1]


input = sys.stdin.readline

N = int(input())

low_num = sys.maxsize
max_num = -1

arr = []
for _ in range(N):
    l = list(map(int, input().split(" ")))
    if low_num > min(l):
        low_num = min(l)
    if max_num < max(l):
        max_num = max(l)
    arr.append(l)


def bfs(y,x):
    que = deque()
    visited[y][x] = 1
    que.append((y,x))

    while que:
        y,x = que.popleft()
        for i in range(4):
            dy = y + sy[i]
            dx = x + sx[i]
            if (0<=dy<N) and (0<=dx<N):
                if visited[dy][dx] == 0 and lands[dy][dx] == 1:
                    que.append((dy,dx))
                    visited[dy][dx] = 1
visited = []
answer = 0

for k in range(low_num, max_num):
    lands = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] > k:
                lands[i][j] = 1
    result = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and lands[i][j] == 1:
                bfs(i,j)
                result += 1
    answer = max(answer, result)

print(answer)