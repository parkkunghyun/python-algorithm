import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int, input().split(" "))

que = deque()
que.append(n)

limit = [0] * (100001)
visited = [0] * (100001)


while que:
    x = que.popleft()
    visited[x] = 1
    
    if x == k:
        print(limit[k])
        break
    
    for nextX in (x*2, x-1, x+1):
        if 0 <= nextX < 100001 and visited[nextX] == 0:
            if nextX == x*2:
                visited[nextX] = 1
                que.append(nextX)
                limit[nextX] = limit[x]
            else:
                visited[nextX] = 1
                que.append(nextX)
                limit[nextX] = limit[x] + 1
