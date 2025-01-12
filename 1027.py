
import sys

# L D B P $
"""
L -> s2로 옮기기
D -> s1로 옮기기
B -> s1에 맨뒤를 삭제하기
P $ -> $를 s1에 추가하기

마지막에 s2는 reverse로 반대로 넣기
"""

arr = list(input().rstrip())

stack1 = arr
stack2 = []

M = int(input())
for _ in range(M):
    word = list(input().rstrip())
    if word[0] == 'P': # 단어 추가
        stack1.append(word[2])
    if word[0] == 'L':
        if len(stack1) > 0:
            moveWord = stack1.pop()
            stack2.append(moveWord)
    if word[0] == 'D':
        if len(stack2) > 0:
            moveWord = stack2.pop()
            stack1.append(moveWord)
    if word[0] == 'B':
        if len(stack1) > 0:
            stack1.pop()
    #print(f's1 -> {stack1}')
    #print(f's2 -> {stack2}')
    
stack2.reverse()
res = ''.join(stack1)
res += ''.join(stack2)
print(res)