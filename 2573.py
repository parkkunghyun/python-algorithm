""" 
동서남북에 0이 있는 만큼 빼주기
그리고 두조각 이상 되면 바로 멈추기 그 년도 구하는거
"""

import sys
from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

input = sys.stdin.readline

N,M = map(int, input().split(" "))
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split(" "))))

ans = 0

def bfs(visited, sy,sx):
    que = deque()
    que.append((sy,sx))
    visited[sy][sx] = 1
    while que:
        sy,sx = que.popleft()
        for k in range(4):
            cy = sy + dy[k]
            cx = sx + dx[k]
            if visited[cy][cx] == 0 and arr[cy][cx] > 0:
                visited[cy][cx] = 1
                que.append((cy,cx))

for year in range(1,9999):
    temp = [[0 for _ in range(M)] for _ in range(N)]
    # 년도 체크
    for i in range(1, N):
        for j in range(1,M):
            if arr[i][j] > 0:
                cnt = 0
                for k in range(4):
                    sy = i + dy[k]
                    sx = j + dx[k]
                    if arr[sy][sx] == 0:
                        cnt += 1
                temp[i][j] = max(arr[i][j] - cnt, 0)
    arr = temp
    visited = [[0 for _ in range(M)] for _ in range(N)]
    subCheck = 0
    
    # print()
    # print(f'dssd')
    # for i in range(N):
    #         for j in range(M):
    #             print(arr[i][j], end=" ")
    #         print()
        
    for i in range(1, N):
        for j in range(1,M):
            if visited[i][j] == 0 and arr[i][j] > 0:
                subCheck += 1
                bfs(visited, i,j)
    # print('ccc')
    if subCheck > 1:
        ans = year
        break

# print()
# print()
# for i in range(N):
#         for j in range(M):
#             print(arr[i][j], end=" ")
#         print()
print(ans)

