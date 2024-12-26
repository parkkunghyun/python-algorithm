import sys
from collections import deque
import heapq

input = sys.stdin.readline
INF = sys.maxsize

N,M = map(int, input().split(" "))

arr = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int, input().split(" "))
    arr[a].append((b,c))
    arr[b].append((a,c))

# for i in range(N+1):
#     print(arr[i])

res = [INF] * (N+1)

# def bfs(start):
#     que = deque()
#     que.append(start)
#     res[start] = 0
#     while que:
#         now = que.popleft()
#         for dist, weight in arr[now]:
#             cost = weight + res[now]
#             if res[dist] > cost:
#                 res[dist] = cost
#                 que.append(dist)

# bfs(1)
# print(res[N])

def dijkstra(cost, now):
    heap = []
    heapq.heappush(heap, (cost, now))
    res[now] = 0
    while heap:
        prevCost, prevDist = heapq.heappop(heap)
        for dist, weight in arr[prevDist]:
            cost = weight + prevCost
            if res[dist] > cost:
                res[dist] = cost
                heapq.heappush(heap, (cost, dist))
dijkstra(0,1)
print(res[N])