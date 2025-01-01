"""
D
N
12 10000
시작 도착 길이

일단 지름길 도착위치가 넘어가면 거긴 버리기

시작과 도착이 같다면 더 짧은애를 선택하기
그 이후 도착위치가 시작위치인애 찾기 -> 없으면 다음 작은 시작 위치까지 더하기
이거 반복 후 계산하기

시작하고 도착 뺀거보다 길이가 더 크면 버리기

"""

import sys

input = sys.stdin.readline

N, D = map(int, input().split(" "))
graph = []

for _ in range(N):
    graph.append(list(map(int, input().rstrip().split(" "))))

distance = [i for i in range(D+1)] # 0 - 101

for i in range(D+1):
    distance[i] = min(distance[i], distance[i-1]+1)
    print(f"distance[i] => {distance[i]}")
    for start, end, dist in graph:
        if i == start and end <= D and distance[i] + dist < distance[end]:
            distance[end] = distance[start] + dist
            print(f"dddd ->  {distance[end]}")