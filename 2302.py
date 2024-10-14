"""
v가 되어 있는데 제외하고 각각 서로 움직일수있는 만큼 움직이고 곱하기
피보나치??
1 -> 1
2 -> 2
3 -> 3
4 -> 5
5 -> 8
6 -> 13

40까지 피보나치를 구해서
v가 아노는 영역을 구하기 그래서 각가 빼주면 될듯?

1 2 3 4 5 6 7 8 9
1 2 3 v 5 6 v 8 9

3 - 0

"""

import sys

input = sys.stdin.readline

# 피보나치 40까지 구하기
arr = [0 for i in range(41)]
arr[0] = 1
arr[1] = 1
arr[2] = 2

for i in range(3, 41):
    arr[i] = arr[i-1] + arr[i-2]

n = int(input())
m = int(input()) # 0 - n

l = [0 for _ in range(n+1)]

for _ in range(m):
   ml = int(input())
   l[ml] = -1

answer= 1

#print(arr)
#print(l)

# v가 아닐때까지 개수 세기
check = 1
i = 1

# 1 2 3 4 5 6 7 8 9
# 1 2 3 v 5 6 v 8 9

while i < n+1:
    if l[i] == -1:  # vip
        answer *= arr[i - check]
        #print(f'check -> {check} i -> {i}')
        check = i + 1
    i += 1


#print(f'last check -> {check}')
answer *= arr[n+1-check] 
print(answer)

