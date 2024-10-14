"""
다사다난하게 quack가 되었으면 그건 무조건 별개 한마리

근데 quack quack로 되어있으면 그건 하나로 퉁치기


"""

import sys
from collections import deque

input = sys.stdin.readline

sound = deque(input().rstrip())

check = 0 # 다사다난하게 들어왔는지
# 만약 그랬다면 1로 바꾸고 하나 끝나면 다시 0으로 교체!

# 아니면 일단 list하고 q나오면 deque담기
# quack로 되면 그건 하나로 침 근데 중간에 다른거 있었을때는 check를 변형해서 1마리 아닌걸로!

answer = 0

while sound:
    s = sound.popleft()
    if 
    
if (answer ==0):
    print(-1)
else:
    print(answer)