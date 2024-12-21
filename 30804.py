import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(" ")))

dict = {}
cnt = 0

ans = 0
left = 0

for right in range(N):
    if arr[right] in dict:
        dict[arr[right]] += 1
    else:
        dict[arr[right]] = 1
        cnt += 1
    if cnt > 2:
        while cnt > 2:
            #print(right, left, dict, cnt)
            dict[arr[left]] -= 1
            if dict[arr[left]] == 0:
                cnt -= 1
                del dict[arr[left]]
            left += 1
    ans = max(ans, right - left + 1)
print(ans)