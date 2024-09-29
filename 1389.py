
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start): # 시작위치
    que = deque()
    box = [0 for _ in range(N+1)] # 0 0 0 0 0 0
    
    que.append(start) # 1
    box[start] = 1
    
    while que: # 
        n = que.popleft() # 1
        #print(f'n -> {n}')
        for i in l[n]: # 3,4
            if box[i] == 0: # 3 
                box[i] = box[n] + 1
                que.append(i)
    for i in range(1, N+1):
        box[i] -=1
    return sum(box)

N,M = map(int, input().split(" "))

l = [[] for _ in range(N+1)]

for _ in range(M):
    A,B = map(int, input().split(" "))
    l[A].append(B)
    l[B].append(A)

box = []

for i in range(1,N + 1):
    data = bfs(i)
    box.append(data)
    
res = 0
d = 99999999
for index, value in enumerate(box):
    if d > value:
        d = value
        res = index
print(res + 1)