import sys
from collections import deque

input = sys.stdin.readline

F,S,G,U,D = map(int, input().split(" "))

arr = [0 for _ in range(F+1)] # 0 0 0 0 0 0 0 0 0 0 0

arr[S] = 1 # 0 1 0 0 0 0 0 0 0 0 0

def bfs():
    que = deque()
    que.append(S)

    while que:
        st = que.popleft()
        if st == G:
            return arr[G]
        for i in (st+U, st-D):
            if 1<= i <=F and arr[i] == 0:
                arr[i] = arr[st] + 1
                que.append(i)
bfs()

if arr[G] == 0:
    print("use the stairs")
else:
    print(arr[G] - 1)
