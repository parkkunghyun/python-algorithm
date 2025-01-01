"""
2 n

즉 서로 뽑았을때 그게 연결되어야함
bfs?

자기가 자기를 가리키는 애들은 무조건 뽑기

서로가서로를 가리킨다고 했을때
그 숫자가 들어있는지 확인하기


"""

import sys

input = sys.stdin.readline

N = int(input())
arr = [0 for _ in range(N+1)]
for i in range(1, N+1):
    arr[i] = int(input())

def dfs(num):
    if visited[num] == False:
        visited[num] = True
        for a in arr[num]:
            tmp_up.add(num)
            tmp_bottom.add(a)
            if tmp_bottom == tmp_up:
                ans.ex
            

ans = []
for i in range(1, N+1):
    visited = [False] * (N+1)
    tmp_up = set()
    tmp_bottom = set()

    dfs(i)

ans = list(set(ans))



