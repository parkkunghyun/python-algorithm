
import sys

input = sys.stdin.readline

N, X = map(int, input().split(" "))

l = list(map(int, input().split(" ")))

if max(l) == 0:
    print("SAD")
else:
    answer_num = sum(l[:X])
    answer_check = 1
    value = answer_num

    for i in range(X, N):
        value +=l[i]
        value -= l[i-X]
        if answer_num < value:
            answer_num = value
            answer_check = 1
        elif answer_num == value:
            answer_check += 1
    print(answer_num)
    print(answer_check)
    