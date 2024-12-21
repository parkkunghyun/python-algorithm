"""
h
작거나 같으느 높이만 먹기 가능
능
L -> 최대 길이 구하기

10 11 13
일단 1만개 있음 -> 이거 순서대로 아님

1. 알던 현재 내 값보다 작거나 같다 -> 그러면 먹기기능 +1
2. 정렬해줘야함 ->
3. 그러면 10000까지의 배열을 만들고 
거기에 데이터 넣기
그리고 해당 값들을 먹을 수 있으면 계속 증가 시키기!

나보다 작은 애들 개수 세기
일단 도는데 나보다 작은 애들이 1이다 그러면 나 +1하기
계속 비교!! 1만까지해 걍
"""

import sys

input = sys.stdin.readline

N,L = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

dp = [0] * (10001)

for a in arr:
    dp[a] += 1

temp = L # 1
i = 1

while True:
    if i == len(dp):
        break
    if i <= temp and dp[i] >= 1:
        temp += 1
        dp[i] -= 1
    else:
        i += 1

print(temp)