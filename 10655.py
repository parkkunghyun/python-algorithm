import sys
input = sys.stdin.readline

def distance(a, b) :
  return abs(coord_list[a][0] - coord_list[b][0]) + abs(coord_list[a][1] - coord_list[b][1])

N = int(input())
coord_list = [list(map(int, input().split())) for _ in range(N)]
max_diff = -float('inf')
result = 0
for i in range(N-1) :
  dist = distance(i, i+1)
  result += dist

print(result)