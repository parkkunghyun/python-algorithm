"""
ABRACADABRA
ECADADABRBCRDARA

각각 투포인터를 적용해서
해당 단어의 부분이 있는지 확인!

"""

import sys

input = sys.stdin.readline

first = input().rstrip()
second = input().rstrip()

result = 0

dp = [[0 for _ in range(len(second) + 1)] for _ in range(len(first) + 1)]

answer = 0

for i in range(1, len(first) + 1):
    for j in range(1, len(second) + 1):
        if first[i-1] == second[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        answer = max(answer, dp[i][j])
print(answer)