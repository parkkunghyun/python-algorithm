"""
같은 칸을 하나 만들기
0 0 0 0 0
0 0 0 0 0


"""
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    l = []
    l.append(list(map(int, input().split(" "))))
    l.append(list(map(int, input().split(" "))))
