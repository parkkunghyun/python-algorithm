"""
매수 - 사는거
매도 - 파는거

마지막날 남은 현금을 보는건데

dp? 스타일로 풀수있을듯

1. 그냥현금
2. 전에 산거랑 판거
3. 

dp[0]
dp[i] = max(dp[])


"""

import sys

input = sys.stdin.readline

n,w = map(int, input().split(" "))
days=[]
for i in range(n):
    days.append(int(input()))
