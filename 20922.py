import sys

input = sys.stdin.readline

right,left = 0,0
answer = 0

N,K = map(int, input().split(" "))
l = list(map(int, input().split(" ")))

days = [0 for _ in range(1, N+1)]

while right < N:
    if days[l[right]] < K:
        days[l[right]] += 1
        right += 1
    else:
        days[l[left]] -= 1
        left += 1
answer = max(answer, right-left)
print(answer)