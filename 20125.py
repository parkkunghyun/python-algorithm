
N = int(input())
l = []

for i in range(N):
    line = input()
    l.append(list(line))

# 일단 머리 찾고 심장 찾기
find = False
heartX = 0
heartY = 0

for i in range(N):
    for j in range(N):
        if l[i][j] == '*':
            heartY = i + 1
            heartX = j
            find = True
            break
    if find == True:
        find = False
        break

leftArm = 0
rightArm = 0
waist = 0
leftLeg = 0
rightLeg = 0
# 이제 팔 길이 구하기
# 2,2
for i in range(heartX-1, -1, -1):
    if l[heartY][i] == '*':
        leftArm += 1
    else:
        break

for i in range(heartX+1, N):
    if l[heartY][i] == '*':
        rightArm += 1
    else:
        break

for i in range(heartY+1, N):
    if l[i][heartX] == '*':
        waist += 1
    else:
        break

# 왼다리
uY = heartY + waist + 1
uX = heartX - 1

for i in range(uY, N):
    if l[i][uX] == '*':
        leftLeg += 1
    else:
        break

uX = heartX + 1
for i in range(uY, N):
    if l[i][uX] == '*':
        rightLeg += 1
    else:
        break
print(heartY+1, heartX+1)
print(leftArm, rightArm, waist, leftLeg, rightLeg)
# 오른다리
# 다리 구하기

# 정답 작성 -> 심장 1씩 더하기!

    
