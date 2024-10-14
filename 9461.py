"""
현재 값에서 전부 뒤져도 안걸리긴함

부분 수열이다 보니 음..
0 4 0 1 1 0
1 1 2 2 2 3

일단 체크값저장
직전값과 지금 보는 값을 비교
거기서 체크값 > n >

1 1 2 2 2 3
1 1 2 2 2 3

1 1 1 1 1 1
10 30 10 20 20 10

"""

import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(" ")))

answer = 0

dp = [1 for _ in range(N)]

for i in range(1, len(arr)):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))