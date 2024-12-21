"""
삼각형의 기준
밑변을 기준으로 양 사이드가 같다

밑변이 양변보다 크면 안됨!

양면이 1이상 차이나면 안됨
1 - 0
2 - 0
3 - 1
4 - 0
5 - 1 => 221 
6 - 1 => 222 123
7 -  => 133 
8 - 


"""

import sys
input = sys.stdin.readline

n = int(input())

res = 0
for i in range(1,n+1): # 가장 짧은변
    for j in range(i, n+1):
        k = n - i - j
        if k >= i + j:
            continue
        else:
            if j > k:
                break
            res += 1
print(res)