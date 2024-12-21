import sys
from collections import deque

input = sys.stdin.readline

N,d,k,c = map(int, input().split(" "))

belt = []
for _ in range(N):
    belt.append(int(input()))

result = 0
cnt = 0
eat = deque()

for i in range(k-1):
    eat.append(belt[i])

for j in range(N):
    eat.append(belt[(j + k - 1) % N] )
    cnt = 0
    if c not in eat:
        cnt = 1
    result = max(result, len(set(eat)) + cnt)
    eat.popleft()
print(result)