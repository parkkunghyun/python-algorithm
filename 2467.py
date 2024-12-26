"""
26분시작

가장 큰 경우 -> N**2
일단 정렬해서 들어옴 -> 투포인터 사용하기? 
중간을 기준으로 계산?

0이랑 계산해서 절댓값으로 가장 작은애가 winner


"""

import sys

input = sys.stdin.readline

N = int(input())
liquids = list(map(int, input().split(" ")))

left_idx = 0
right_idx = N-1

ans = abs(liquids[left_idx] + liquids[right_idx])
ans_left_idx = left_idx
ans_right_idx = right_idx

while ans_left_idx < ans_right_idx:
    temp = liquids[ans_left_idx] + liquids[ans_right_idx]

    if abs(temp) < ans:
        ans = abs(temp)
        left_idx = ans_left_idx
        right_idx = ans_right_idx

    if temp == 0:
        break
    if temp <= -1:
        ans_left_idx += 1
    if temp >= 1:
        ans_right_idx -= 1

print(liquids[left_idx], liquids[right_idx])