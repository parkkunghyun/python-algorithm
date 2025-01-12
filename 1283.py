
import sys

input = sys.stdin.readline

alpha_exist = []

N = int(input())
for _ in range(N):
    words = list(input().rstrip().split(" "))
    
    flag = False # 일단 먼저 첫글자들 확인하기!
    for i in range(len(words)):
        if words[i][0].upper() not in alpha_exist:
            alpha_exist.append(words[i][0].upper())
            words[i] = "[" + words[i][0] + "]" + words[i][1:]
            flag = True
        if flag == True:
            break
    if flag: # 여기서 출력하기
        print(" ".join(words))
    else: # 모든 단어 확인하기!!
        flag = False
        for w in range(len(words)):
            check = False
            for k in range(len(words[w])):
                if words[w][k].upper() not in alpha_exist:
                    alpha_exist.append(words[w][k].upper())
                    words[w] = words[w][:k] + "[" + words[w][k] + "]" + words[i][k+1:]
                    check = True
            if check == True:
                break
        print(" ".join(words))