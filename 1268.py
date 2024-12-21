import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split(" "))))

# print()
# for i in range(n):
#     for j in range(5):
#         print(arr[i][j], end= " ")
#     print()
# print()

s = 0
answer = 0

# 지금부터 index로 내림

for i in range(n):
    temp = 0
    students = [0] * (n+1)
    for j in range(5):
        for k in range(n):
            if arr[k][j] == arr[i][j] and k != i:
                students[k] = 1
                temp += 1
    if answer < temp:
        answer = temp
        s = i
print(s + 1)