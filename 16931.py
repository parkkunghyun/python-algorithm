"""
중간 비어있는걸 세어줘야함!!

그러니까 즉 면이 보이면 그걸 넣기!

가로로 보기 만약 가장 긴게 있다 그러면 무조건 그거
근데 중간에 앞과 뒤가 뚫려있는지 확인해야함!!

일단 위아래 해서 -> nm * 2해주기

점점 커지는게 아니라 중간에 줄었다가 커지면 
현재 높이랑 다음꺼 보고 차이만큼 추가해주기!

"""

import sys

input = sys.stdin.readline

N,M = map(int, input().split(" "))

arr = []
for _ in range(N):
    l = list(map(int, input().split(" ")))
    arr.append(l)

side1 = 0
side2 = 0
side3 = N * M

for i in range(N):
    for j in range(M):
        if j == 0: #맨 앞면일때
            side1 += arr[i][j]
        else:
            if arr[i][j] > arr[i][j-1]:
                side1 += arr[i][j] - arr[i][j-1]

for j in range(M):
    for i in range(N):
        if i == 0: #맨 앞면일때
            side2 += arr[i][j]
        else:
            if arr[i][j] > arr[i-1][j]:
                side2 += arr[i][j] - arr[i-1][j]

print((side1 + side2 + side3)*2)