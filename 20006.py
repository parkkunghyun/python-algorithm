
import sys

input = sys.stdin.readline

p,m = map(int, input().split())

# l = []
rooms = []
for _ in range(p):
    l, n = input().strip().split(" ")
    l = int(l)
    if len(rooms) == 0:
        room = [[l, n]] # 
        rooms.append(room)
        print(room[0][0])
    else:    
        flag = False
        for r in rooms:
            if r[0][0] - 10 <= l <= r[0][0] + 10:
                if len(r) < m:
                    flag = True
                    r.append([l,n])
        if flag == False:
            room = [(l,n)]
            rooms.append(room)

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    room = sorted(room, key=lambda x : x[1])
    for r in room:
        print(r)