import sys

input = sys.stdin.readline

# 입력 처리
N = int(input())
arr = list(map(int, input().rstrip().split()))

# 배열 정렬
arr.sort()

cnt = 0

# 투포인터로 탐색
for i in range(N):
    num = arr[i]
    left, right = 0, N - 1

    while left < right:
        if left == i:  # 현재 수는 건너뛰기
            left += 1
            continue
        if right == i:  # 현재 수는 건너뛰기
            right -= 1
            continue

        total = arr[left] + arr[right]
        if total == num:
            cnt += 1
            break
        elif total < num:
            left += 1
        else:
            right -= 1

print(cnt)
