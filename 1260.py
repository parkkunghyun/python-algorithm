"""
정점 번호 작은것부터 먼저 방문
4 5 1
1 - 4
1 2 3 4
2 4
3 4


"""

import sys
from collections import deque

input = sys.stdin.readline

N,M,V = map(int,input().split(" "))

arr = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    start, dst = map(int , input().split(" "))
    arr[start].append(dst)
    arr[dst].append(start)
# bfs
def bfs(start):
    que = deque()
    que.append(start)
    visited[start] = 1
    while que:
        s = que.popleft()
        print(s, end=" ")
        # 하기전에 한번 정렬!
        arr[s].sort()
        for i in arr[s]:
            if visited[i] == 0:
                visited[i] = 1
                que.append(i)

# dfs
visited = [0 for _ in range(N+1)]
def dfs(visited, start):
    print(start, end=" ")
    arr[start].sort()
    for i in arr[start]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(visited, i)
            #visited[i] = 0

visited[V] = 1
dfs(visited, V)
print()
visited = [0 for _ in range(N+1)]
bfs(V)