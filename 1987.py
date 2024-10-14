"""
R C
상하좌우
같은 알파벳칸이 적힌칸을 못감
말이 최대 몇칸 갈 수 있는지 정하기

깊이 탐색이 나을라나?
"""

import sys
from collections import deque

R,C = map(int, input().split(" "))

cy = [-1,1,0,0]
cx = [0,0,-1,1]

arr = []
alpha = [0 for _ in range(26)]
visited = [[0 for _ in range(C)] for _ in range(R)]

result = 1


for _ in range(R):
    l = list(input().rstrip())
    arr.append(l)


# def bfs(y,x):
#     global result
#     que = deque()
#     que.append((y,x))
#     alpha[ord( arr[y][x]) - 65] = 1
#     visited[y][x] = 1
#     while que:
#         sy,sx = que.popleft()
#         for i in range(4):
#             dy = sy + cy[i]
#             dx = sx + cx[i]
#             if 0<= dy < R and 0<= dx < C:
#                 if alpha[ord(arr[dy][dx]) - 65] == 0 and visited[dy][dx] != 1:
#                     alpha[ord(arr[dy][dx]) - 65] = 1
#                     visited[dy][dx] = visited[sy][sx] + 1
#                     que.append((dy,dx))
#                     result += 1
# bfs(0,0)

answer = 1

def dfs(y,x, alpha, visited):
    for i in range(4):
        dy = y + cy[i]
        dx = x + cx[i]
        if 0<= dy < R and 0<= dx < C:
             if alpha[ord(arr[dy][dx]) - 65] == 0 and visited[dy][dx] == 0:
                 alpha[ord(arr[dy][dx]) - 65] = 1
                 visited[dy][dx] = max(visited[dy][dx], visited[y][x] + 1)
                 dfs(dy, dx, alpha, visited)
                 alpha[ord(arr[dy][dx]) - 65] = 0

visited[0][0] = 1
alpha[ord(arr[0][0]) - 65] == 1
dfs(0,0, alpha, visited)
print(visited)