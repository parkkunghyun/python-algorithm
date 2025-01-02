"""
N
단어 첫글자 단축키
첫글자 다 되어있으면 그 다음 단어
다 있으면 그냥 놔두고 대소문자 구분 없음
30

알파벳 배열을 만들기

대소문자 생각안하고 일단 보기!
일단 단어별로 구별하기
맨 처음 단어의 첫 글자는 무조건 괄호가 됨!

일단 전부 다 되면 그러면 그 단어는 그냥 두기

일단 문장이 들어오면 단어단위로 나누기
그리고 단어의 첫글자 보기 -> 다 되어있으면 순서대로 알파벳 돌기! 공백 제외하고!!

"""

import sys

input = sys.stdin.readline

alpha = [0] * (26) # A
# print(chr(97)) -> a
#print(ord('A')) -> 65

N = int(input())

for _ in range(N):
    words = list(input().rstrip().split(" "))
    # 해당 단어들의 첫번째 보기!
    flag = False
    for i in range(len(words)):
        #print(f"first -> {words[i][0]}")
        # 일단 대문자이면서 해당 단어가 체크가 안되어있을때!
        if 'A' <= words[i][0] <= 'Z' and alpha[ord(words[i][0]) - 65] == 0:
            # 괄호 치고 프린트하고 for문 나가기
            alpha[ord(words[i][0]) - 65] = 1
            new_word = "[" + words[i][0] + "]"
            for w in range(1, len(words[i])):
                new_word += words[i][w]
            words[i] = new_word
            flag = True
            break
        # 소문자일때
        if 'a' <= words[i][0] <= 'z' and alpha[ord(words[i][0]) - 97] == 0:
            # 괄호 치고 프린트하고 for문 나가기
            alpha[ord(words[i][0]) - 97] = 1
            new_word = "[" + words[i][0] + "]"
            for w in range(1, len(words[i])):
                new_word += words[i][w]
            words[i] = new_word
            flag = True
            break
    # 즉 괄호가 추가되었을때
    if flag:
        print(' '.join(words))
    else:
        flag = False
        result = ""
        # 여기서부터는 처음부터 글자 살피기
        full = " ".join(words)
        for i in range(len(full)):
            if 'a' <= full[i] <= 'z' and alpha[ord(full[i]) - 97] == 0:
                alpha[ord(full[i]) - 97] = 1
                full = full.replace(full[i], "[" + full[i] + "]")
                flag = True
                break
            if 'A' <= full[i] <= 'Z' and alpha[ord(full[i]) - 65] == 0:
                alpha[ord(full[i]) - 65] = 1
                full = full.replace(full[i], "[" + full[i] + "]")
                flag = True
                break
        print(full)