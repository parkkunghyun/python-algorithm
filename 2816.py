import sys

input = sys.stdin.readline

N = int(input())
channels = []
for _ in range(N):
    channels.append(input().rstrip())

# 그러면 일단 kbs1부터 찾기!
# 만약 kbs1이 나올때까지 돌리기
# 그리고 만약에 kbs2가 먼저 나왔다!! -> 그러면 그때는 비상이긴해
# 일단 둘 중에 하나 먼저 쭉 내려서 찾고 그 다음꺼 쭉 내려서 찾기 어떤데

ans = ''
curr = 0
while channels[curr] != 'KBS1':
    curr += 1
    ans += '1'
for _ in range(curr):
    ans += '4'
curr = 0
channels.remove('KBS1')
channels = ['KBS1'] + channels
while channels[curr] != 'KBS2':
    curr += 1
    ans += '1'
for _ in range(curr-1):
    ans += '4'

print(ans)