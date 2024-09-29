"""
n m 
11
nm

아래 오른 대각선 아래
사탕의 최댓값 구하기! -> dfs? bfs?
0,0 -> N-1, M-1

어떻게 푸는지
    바깥을 0으로 패딩을 채우기 ! -> 그리고 각 단계를 갈때마다 최댓값을 구하기
    3방향 중 max값을 구하기!
    
    dp[i][j] ~ dp[N][M]까지!
    
어디서 잘못 생각했는지
    재귀를 1000번하면 무조건 걸림! -> 재귀는 100이하만
    방문해서 간다라고 하면 그 문제는 DP로 풀 수 있다! -> 한단계씩 갈때
뭘 배웠는지


"""

# def check(sY, sX, candies):
#     global result
#     if sY == N-1 and sX == M-1:
#         if result < candies:
#             result = candies + l[sY][sX]
#         return
#     if sY < N and sX < M:
#         check(sY+1, sX+1, candies + l[sY][sX])
#         check(sY+1, sX, candies + l[sY][sX])
#         check(sY, sX+1, candies + l[sY][sX])
#     else:
#         return

N,M = map(int, input().split(" "))
l = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    line = list(map(int, input().split(" ")))
    for j in range(1,M+1):
        l[i][j] = line[j-1]
#print(l)



# 시작은 1,1부터!
for i in range(1, N+1):
    for j in range(1, M+1):
        maxNum = max(l[i-1][j], max(l[i][j-1], l[i-1][j-1]))
        l[i][j] += maxNum
print(l[N][M])
        

# for _ in range(N):
#     line = list(map(int, input().split(" ")))
#     l.append(line)
#print(l)