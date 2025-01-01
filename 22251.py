"""
k에 맞춰서 보여주기
1 p
1 -> 2로 바꾸는데 5개 led반전
반전 이후 다시 올바르게 보이게 하기
x층에 멈췄을때 반전시킬 led를 고를 수 있는 경우의 수

1-N
k - 보여줄 숫자의 길이
x - 멈춘 층

"""

import sys

input = sys.stdin.readline

N,K,P,X = map(int, input().split(" "))

