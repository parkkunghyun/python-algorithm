import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    if N < 10:
        print(1)
    else:
        cnt = 0
        flag = True
        while N != 1 and flag:
            flag = False
            for i in range(9,1,-1):
                if N % i == 0:
                    cnt += 1
                    N //= i
                    flag = True
                    break
            if flag == False and N >= 10:
                break
        if flag == False:
            print(-1)
        else:
            print(cnt)