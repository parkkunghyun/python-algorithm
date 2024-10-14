"""
N - A 1 - n
M
10만 정렬하면 초과뜨나?
정렬하고 이분탐색 ㄱ?

"""

N = int(input())
A = list(map(int, input().split(" ")))

M = int(input())
mList = list(map(int, input().split(" ")))

A.sort()

for m in mList:
    result = 0
    start = 0
    end = len(A)-1 # 1 2 3 4   5
    while start <= end:
        mid = (start + end) // 2 # 2
        if A[mid] == m: #
            result = 1
            break
        elif A[mid] < m: # 3 
            start = mid + 1
        else:
            end = mid - 1 # 2
    print(result)
