"""
1-n

1234
3000개
현재 맨앞의 숫자를 기준으로
그 수보다 작거나 같으면 자리수 올리기


"""
import sys

input = sys.stdin.readline

nums = input().rstrip()

result = 0
idx = 0

while True:
    result += 1
    for s in str(result):
        if nums[idx] == s:
            idx += 1
            if idx >= len(nums):
                print(result)
                exit()
