"""
N
하나의 수를 제곱했을때 그 수가 맨뒤에 똑같이 나오는지 확인

그러면 문자열로 보기?
"""

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    res = N*N
    ln = list(str(N)) # 76
    res = list(str(res)) # 5776
    
    res = res[-len(ln):]
    
    flag = True
    for i in range(len(ln)):
        if ln[i] != res[i]:
            flag = False
            break
    
    if flag == False:
        print("NO")
    else:
        print("YES")