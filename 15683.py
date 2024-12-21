"""
1 한개
2 반대
3 직각
4 3방향
5 네방향
회전은 90도 가로 또는 세로
6은 벽 즉 6이거나 끝까지 가면 막힘
사각지대의 최소크기 정하기

매번 확인하기!
각 방향에 대해 움직일 수 있는 방법을 지정하기

각 경우의 수를 구하기
그 다음 각 방법으로 돌려주기
그리고 빈칸 개수 세기
이때 최소이면 그걸로 적용하기

4가지 2가지 4가지 4가지 1가지

/usr/bin/python3 /Users/baggyeonghyeon/Desktop/web/solvedac/15683.py
"""

import sys

input = sys.stdin.readline

one = [(1,0), (-1,0), (0,-1), (0,1)]

N,M=map(int, input().split(" "))
office = []

for _ in range(N):
    office.append(list(map(int, input().split(" "))))

