"""

"""

import sys
from collections import deque

def dfs(n, idx, rst):
    #print(f'idx -> {idx}')
    if idx == n:
        ans = eval(rst.replace(' ', ''))
        if ans == 0:
            arr.append(rst)
    else:
        n_idx = idx + 1
        dfs(n, n_idx, rst + ' ' + str(n_idx))
        dfs(n, n_idx, rst + '+' + str(n_idx))
        dfs(n, n_idx, rst + '-' + str(n_idx))

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = []
    dfs(N, 1, '1')
    for a in arr:
        print(a)
    print()