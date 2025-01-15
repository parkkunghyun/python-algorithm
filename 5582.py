"""
ABRACADABRA
ECADADABRBCRDARA

각각 투포인터를 적용해서
해당 단어의 부분이 있는지 확인!

그래서 길이가 더 큰걸 저장하기

해당 문자로 시작
그리고 해당 길이까지를 보기
그런데 그거 없으면 패스

그 다음 줄로 넘어가기
"""

import sys

input = sys.stdin.readline

first = input().rstrip()
second = input().rstrip()

result = 0

for i in range(len(first)):
    