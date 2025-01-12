"""
상하좌우
장애물 막히기전까지 볼 수 있음
T S O
3개의 장애물

음 장애물을 설치하고 해당 선생이 보지 못하는지 매번 환인?
YES NO

선생하고 붙어있으면 바로 No

"""

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
teacher = []

def backTracking(cnt):
    global flag
    
    if cnt == 3:
        if bfs():
            flag = True
            return
    else:
        for x in range(n):
            for y in range(n):
                if arr[x][y] == 'X':
                    arr[x][y] = 'O'
                    backTracking(cnt+1)
                    arr[x][y] = 'X'
def bfs():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    for t in teacher:
        for k in range(4):
            nx, ny = t
            while 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 'O':
                    break
                if arr[nx][ny] == 'S':
                    return False
                nx += dx[k]
                ny += dy[k]
        return True

arr = []
flag = False

for i in range(n):
    arr.append(list(input().rstrip().split(" ")))
    for j in range(n):
        if arr[i][j] == 'T':
            teacher.append([i,j])

backTracking(0)

if flag:
    print("YES")
else:
    print("NO")
