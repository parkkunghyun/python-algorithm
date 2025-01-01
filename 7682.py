"""
o가 이겼다 => x == o랑 개수가 같음
x가 이겼다 => x가 o보다 1개 많음

만약 x o상관없이 다 찼다 -> x5개 o4개 그리고 그 전에 x나 o가 이긴게 없어야함
"""

import sys

input = sys.stdin.readline

def check(arr, equ):
    if arr[0][0] == arr[0][1] == arr[0][2] == p:
        return True
    if arr[1][0] == arr[1][1] == arr[1][2] == p:
        return True
    if arr[2][0] == arr[2][1] == arr[2][2] == p:
        return True
    if arr[0][0] == arr[1][0] == arr[2][0] == p:
        return True
    if arr[0][1] == arr[1][1] == arr[2][1] == p:
        return True
    if arr[0][2] == arr[1][2] == arr[2][2] == p:
        return True
    if arr[0][0] == arr[1][1] == arr[2][2] == p:
        return True
    if arr[0][2] == arr[1][1] == arr[2][0] == p:
        return True
    return False

while True:
    T = input().rstrip()
    if T == "end":
        break
    arr = [[0,0,0], [0,0,0], [0,0,0]]
    xcnt = 0
    ocnt = 0
    index = 0
    for i in range(3):
        for j in range(3):
            arr[i][j] = T[index]
            if T[index] == 'X':
                xcnt += 1
            if T[index] == 'O':
                ocnt += 1
            index += 1
    # 2개이상 많으면 invalid
    if xcnt > ocnt + 1:
        print("invalid")
        continue
    if ocnt > xcnt:
        print("invalid")
        continue
    if ocnt == xcnt: #o가 이겼어야함!
        if check(arr, "O") and not check(arr, "X"):
            print("valid")
            continue
    if ocnt + 1 == xcnt: #x가 이겼어야함!
        if check(arr, "X") and not check(arr, "O"):
            print("valid")
            continue
    if xcnt == 5 and ocnt == 4:
        if not check(arr, "O"):
            print("valid")
            continue
    print("invalid")