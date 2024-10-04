"""
다른색깔 볼 뛰어넘기 가능
옮기는건 하나의 색깔

최소로 옮기기 -> 즉 여러번 옮겨보면서 정하기

즉 각 색깔이 서로 끝에 있어야함 -> !!
일단 파랑이나 레드중 끝에 있는걸 찾기
각 색깔을 한쪽으로 밀기

1. 만약 끝에 있다면?
    그때는 글로 전부 옮기기
2. 없다면?
    그 공의 개수를 세기 -> 그게 정답임
"""

import sys

input = sys.stdin.readline

N = int(input())

line = list(input().rstrip())

answer = sys.maxsize

# 파랑
blue_check1 = 0
if line[0] == 'B' or line[N-1] == 'B':
    # 어디까지 B인지 확인
    if line[0] == 'B':
        check = 1
        for i in range(1, N):
            if line[i] == 'B':
                check+=1
            else:
                break
        # 그러면 기서 부터 이제 각 B의 개수를 세기!
        for i in range(check, N):
            if line[i] == 'B':
                blue_check1 += 1
        if answer > blue_check1:
            answer = blue_check1
        blue_check1 = 0
    if line[N-1] == 'B': # 오른쪽 끝
        check = 1
        for i in range(N-2, -1,-1):
            if line[i] == 'B':
                check+=1
            else:
                break
        # 그러면 여기서 부터 이제 각 B의 개수를 세기!
        for i in range(N-check-1, -1, -1):
            if line[i] == 'B':
                blue_check1 += 1
        if answer > blue_check1:
            answer = blue_check1
else:
    for i in range(N):
        if line[i] == 'B':
            blue_check1 += 1
    if answer > blue_check1:
            answer = blue_check1
#print(f'blue -> {answer}')

####

red_check1 = 0
if line[0] == 'R' or line[N-1] == 'R':
    # 어디까지 R인지 확인
    if line[0] == 'R':
        check = 1
        for i in range(1, N):
            if line[i] == 'R':
                check+=1
            else:
                break
        # 그러면 기서 부터 이제 각 B의 개수를 세기!
        for i in range(check, N):
            if line[i] == 'R':
                red_check1 += 1
        if answer > red_check1:
            answer = red_check1
        red_check1 = 0
    if line[N-1] == 'R': # 오른쪽 끝
        check = 1
        for i in range(N-2, -1,-1):
            if line[i] == 'R':
                check+=1
            else:
                break
        for i in range(N-check-1, -1, -1):
            if line[i] == 'R':
                red_check1 += 1
        if answer > red_check1:
            answer = red_check1
else:
    for i in range(N):
        if line[i] == 'R':
            red_check1 += 1
    if answer > red_check1:
            answer = red_check1

print(answer)
