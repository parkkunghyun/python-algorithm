import sys

input = sys.stdin.readline

N = int(input())

arr = []
teachers = []
dy = [-1,1,0,0]
dx = [0,0,1,-1]
flag = False

def backTracking(cnt):
    check = False
    global flag
    if cnt == 3:
        check = dfs()
        if check:
            flag = True
        return
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
                backTracking(cnt+1)
                arr[i][j] = 'X'

def dfs ():
    for t in teachers:
        for k in range(4):
            cy, cx = t
            while 0<= cy < N and 0 <= cx < N:
                if arr[cy][cx] == 'O':
                    break
                if arr[cy][cx] == 'S':
                    return False
                cy += dy[k]
                cx += dx[k]
    return True

for i in range(N):
    arr.append(list(input().rstrip().split(" ")))
    for j in range(N):
        if arr[i][j] == 'T':
            teachers.append([i,j])

#print(teachers)
backTracking(0)

if flag:
    print("YES")
else:
    print("NO")