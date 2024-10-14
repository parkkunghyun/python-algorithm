"""
K
아이디 문제번호 점수
그 중 최고점수가 최종 점수 -> 제출되는 시간 순서

없으면 그 문제 0점

우리 팀 -> 각문제에 대해 받은 점수 총합
높은 점수 받은 팀 + 1

풀이 횟수 > 마지막 제출시간 더 빠른 팀
점수는 제일높은거, 시간은 제일 늦은걸로

각 팀당 딕셔너리 만들기 -> 최종합도 저장하기

3 4 3 

입력 팀n에 대해 각 팀 만들기
"""

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n,k,t, m = map(int, input().split(" "))
    teams = dict()
    for i in range(1, n+1):
        teams[i] = [0 for _ in range(2)] # 각 부분에 대한 설명
        teams[i].append([0 for _ in range(k+1)]) # 각 문제에 대한 풀이 횟수
    # 최종 합, 마지막 제출시간, 풀이 횟수 
    # 팀, 문제개수, 내팀, 로그(시간)
    for i in range(m):
        id, num, score = map(int, input().split(" "))
        teams[id][0] += score # 총합
        teams[id][1] = i # 제출시간
        teams[id][2][num] += 1
    print(teams)
    # 정렬하기 -> 1. 최종점수 > 