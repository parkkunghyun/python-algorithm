"""
일단 0의 개수를 구하고 1의 개수를 구하기
해당 0

홀수번째 문자는 1 짝수 0

각각을 따로 보고 0이 있으면 가장 앞에 두기
"""

import sys

input = sys.stdin.readline

N = input()

zero_cnt = 0
one_cnt = 0

for i in N:
    if i == '0':
        zero_cnt += 1
    else:
        one_cnt += 1

if zero_cnt > 1:
    zero_cnt /= 2
    zero_cnt = int(zero_cnt)
if one_cnt > 1:
    one_cnt /= 2
    one_cnt = int(one_cnt)

ans = ''

