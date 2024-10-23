"""
100부터 시작으로일단하고
100이 아니면
    아웃된곳이 아니면서 현재 값이 더 작다 그리면 +하고 넘기기
    아웃된곳이 아니면서 현재 값이 더 크다 그러면 -하고 넘기기

시작을 최대한 근처에서 시작하고 싶다
    한자리씩 보기 -> 그래서 현재 자리가 아웃이 아니다 그러면 그자리 채우기
    그리고 아웃이다 그러면 그 근처 돌기 가장 준거 큰거?

"""

import sys
from collections import deque

input = sys.stdin.readline

N = input()
M = int(input())
num = [0 for _ in range(10)]

if M != 0:
    mList = list(map(int, input().split()))
    for ml in mList:
        num[ml] = -1

#print(f'num -> {num}')

def bfs(curr, ):
    que = deque()

if int(N) == 100:
    print(0)
else:
    # 일단 시작 위치 찾기
    current = ""
    temp = N
    N = list(N.rstrip())
    for nl in N:
        #print(f'nl -> {nl}')
        if num[int(nl)] != -1:
            current += nl
        else:
            #print("check")
            # 가장 큰값 8,9
            max_n = 99999 
            for i in range(int(nl), 10):
                if num[i] != -1:
                    max_n = i
                    break
            # 가장 작은값
            min_n = -99999
            for i in range(int(nl), -1, -1):
                if num[i] != -1:
                    min_n = i
                    break

            print(f'max- {max_n} min- {min_n}') #

            if int(nl)-min_n < max_n - int(nl):
                current += str(min_n)
            else:
                current += str(max_n)
    print(f'current -> {current}')
    res = len(N)
    print(f'res -> {res}') # 일단 개수만큼을 더함
    # 이제부터는 + -로 움직이면 됨! 
    # 즉 차이만큼 빼주면 된다!!
    current = int(current)
    #print(abs(int(temp) - current))
    print(res+abs(int(temp) - current) )