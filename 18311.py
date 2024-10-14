"""
n
k

각 해당 왕복 길이를 구해서 그 사이에 있으면 그 번호 출력해주기
일단 전체 길이를 구하기?
아니면 길이당 그 번호만큼을 넣는 배열을 만들기
그리고 한번 더 그 번호만큼 넣기

1 1 1 1 1 1 1 2 2 2 2 3 3 4 4 4 4 5 5 5 5 5
5 5 5 5 5 4 4 4 4

5 28
22

28 -> 22개 초과

28 - 22
6

28
7 4 2 4 5
6
5 4 2

"""

import sys

input = sys.stdin.readline

N,K = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

result = 1

if K <= sum(arr):
    for i in arr:
        K -= i
        if K < 0:
            break
        if K == 0:
            result += 1
            break
        result += 1
else:
    result = len(arr)
    K -= sum(arr)
    for i in range(len(arr)-1, -1, -1):
        K -= arr[i]
        if K <= 0:
            break
        result -= 1

print(result)



# //입력
# 5 7
# 7 4 2 4 5
# //정답
# 2
# 1 1 1 1 1 1 1
# //출력
# 1