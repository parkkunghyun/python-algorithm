"""
일단 x작은순으로 정렬하기!
그리고 

1. 그리고 가장 작은 애 높이 구하기
그거 더하기

2. 다음 x까지 빼기 
그리고 해당 x의 높이로 교체

-> 근데 이때 그 다음 막대가 더 작으면 그냥 해당 높이 유지!
높을때만 교체!

가장 높은데를 기준으로 양 쪽에서 가기?

"""

import sys

input = sys.stdin.readline
N = int(input())

answer = 0

l = [[] for _ in range(N)]
for i in range(N):
    x,y = map(int, input().split(" "))
    l[i].append(x)
    l[i].append(y)
   
l.sort(key=lambda x : x[0])
print(l)

max_height = 0
max_heightI = 0
for i in range(len(l)):
    if max_height < l[i][1]:
        max_height = l[i][1]
        max_heightI = i
print(max_height, max_heightI)

answer += l[0][1] # 4

# 시작 - 높은데
height = l[0][1]
for i in range(1, max_heightI + 1): # 1,2,3,4,
    if height < l[i][1]: 
        height = l[i][1]
    answer += height
print(f"start -> {answer}")

# 끝 - 높은데

answer += max_height
#print(answer)
