"""
모든 참가자 피자 주는 시간
1
1 3 1 4
각 참가자가 필요한 조각

[1 3 1 4]
저 배열만큼 계속 돌고 그 안에가 전부 0이면 답하기

"""

import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(" ")))

time = 0
full = [0] * (N) # 여기에 각 사용자 저장하기

while True:
    # arr내 전부 0이면 그만 돌기
    if sum(arr) == 0:
        break
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] -= 1
            time+=1
            full[i] = time
for t in full:
    print(t, end=" ")
