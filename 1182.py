import sys
from itertools import combinations

input = sys.stdin.readline

N,S = map(int, input().split())
l = list(map(int, input().split()))
answer = 0

# for i in range(1, n+1):
#     comb = combinations(l, i)
#     for x in comb:
#         if sum(x) == s:
#             answer += 1
# print(answer)

def subset_sum(idx, sub_sum):
    global answer
    if idx >= N:
        return
    sub_sum += l[idx]
    if sub_sum == S:
        answer += 1
    subset_sum(idx+1, sub_sum)
    subset_sum(idx+1, sub_sum - l[idx])
subset_sum(0,0)
print(answer)