import sys 

input = sys.stdin.readline

N,M = map(int, input().split(" "))

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split(" "))))

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] + arr[i-1][j-1] - dp[i-1][j-1]

# for i in range(N+1):
#     for j in range(M+1):
#         print(dp[i][j], end=" ")
#     print()
    
k = int(input())
for _ in range(k):
    sy,sx,dy,dx = map(int, input().split(" "))
    cnt = dp[dy][dx] - dp[sy-1][dx] - dp[dy][sx-1] + dp[sy-1][sx-1]
    print(cnt)