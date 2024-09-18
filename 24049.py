n,m = map(int, input().split())
l = [[0 for _ in range(m+1)] for _ in range(n+1) ]

col = list(map(int, input().split()))
row = list(map(int, input().split()))

for i in range(1, n + 1):
    l[i][0] = col[i-1]

for i in range(1, m + 1):
    l[0][i] = row[i-1]

"""
11 -> 01 10
12 -> 02 11
11 -> 
"""
for i in range(1, n+1):
    for j in range(1, m+1):
        if l[i-1][j] == l[i][j-1]:
            l[i][j] = 0
        else:
            l[i][j] = 1
        

print(l[n][m])