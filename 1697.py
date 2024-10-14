"""
사실 K가 더 작다 -> 무조건 -1만 해주면 끝!5 3 => 4 3
K가 더 크다
    *2를 하고 -1을 하는경우
    +1로 찾아가는 경우

"""
import sys
from collections import deque

N,K = map(int, input().split(" "))
visited = [0 for _ in range(100001)]

def bfs(s):
    que = deque()
    que.append(s)
    
    while que:
        cur = que.popleft()
        if 
    

bfs(N)

