"""
4를 만드는 방법 7가지 -> 순서 상관있음
1,2,3을 순서 상관있고 중복 가능하면 순열이다
백트래킹으로 정수 n이 되거나 그거나 크면 패스하기
1 1 1 1
1 1 2

n = 4 0
4 1
4 1 1
4 1 1 1
4 1 1 1 1

4 1 1 1 2
4 1 1 1 3
4 1 1 2
4 1 1 3
4 1 3
"""

import sys
input = sys.stdin.readline

answer = 0

def tracking(n, check):
    global answer
    if check >= n:
        if check == n:
            answer += 1
            return
        else:
            return
    else:
        for i in range(1,4):
            tracking(n, i+check)

T = int(input())
for _ in range(T):
    n = int(input())
    answer = 0
    tracking(n, 0)
    print(answer)

