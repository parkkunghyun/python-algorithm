import sys 

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    l = list(map(int, input().split(" ")))
    max_value = l[-1]
    result = 0 # 최대 차익 계산
    for i in range(N-1, -1, -1): # 
        if max_value < l[i]: # 
            max_value = l[i]
        else:
            result += max_value - l[i]
    print(result)