from collections import deque
import sys

INF = sys.maxsize

def bfs(start):
    q = deque()
    q.append(start)
    dis[start] = 0
    while q:
        #print(f"q -> {q}")
        now = q.popleft()
        for v, w in graph[now]:
            cost = dis[now] + w
            if cost < dis[v]:
                dis[v] = cost
                q.append(v)

N, M = map(int, input().split(" "))
graph = [[] for _ in range(N+1)]
dis = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split(" "))
    graph[a].append((b, c))
    graph[b].append((a, c))

# for i in range(1, N+1):
#     print(graph[i])

bfs(1)
print(dis[N])


# import heapq
# import sys

# INF = sys.maxsize

# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     dis[start] = 0
#     while q:
#         print(f"q -> {q}")
#         d, now = heapq.heappop(q)
#         if dis[now] < d:
#             continue
#         for v,w in graph[now]:
#             cost = d + w
#             if cost < dis[v]:
#                 dis[v] = cost
#                 heapq.heappush(q, (cost, v))
# N,M = map(int, input().split(" "))
# graph = [[] for _ in range(N+1)]
# dis = [INF] * (N+1)

# for _ in range(M):
#     a,b,c = map(int, input().split(" "))
#     graph[a].append((b,c))
#     graph[b].append((a,c))

# for i in range(1,N+1):
#     print(graph[i])

# dijkstra(1)
# print(dis[N]