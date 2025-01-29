import sys
import math

input = sys.stdin.readline

def solve(minHill, maxHill): # 1, 24
    result = 0
    for i in range(N):
        if arr[i] > maxHill:
            result += math.pow(arr[i] - maxHill , 2)
        elif arr[i] < minHill:
            result += math.pow(minHill - arr[i] , 2)
    return result

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

minHill = min(arr)
maxHill = max(arr)

answer = sys.maxsize

for i in  range(minHill, maxHill-17):
    answer = max(answer, solve(i, i+17))

if answer == sys.maxsize:
    print(0)
else:
    print(answer)
