"""

"""

import sys

input = sys.stdin.readline 

def dfs(result, idx, n): # "1", 1, 3
    if idx == n:
        if eval(result.replace(" ", "")) == 0:
            results.append(result)
        return
    empty = result + " " + str(idx + 1)
    plus = result + "+" + str(idx + 1)
    minus = result + "-" + str(idx + 1)
    dfs(empty, idx+1, n)
    dfs(plus, idx+1, n)
    dfs(minus, idx+1, n)

T = int(input())

for _ in range(T):
    n = int(input())
    results = []
    dfs("1", 1, n)
    for result in results:
        print(result)
    print()