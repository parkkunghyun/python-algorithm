"""
40초걸림

일단은 그냥 다 다르다는 기준하에 구해보기 - 이건 아님

그러면 상행과 하행 시간이 같을때도 있다 -> 
각각 시간을 구하고 40초 더한거 안에 들어있는지 확인?
전부 초로 바꿔서 -> 
"""

c,h = map(int, input().split())
cList = []
hList = []

time = 24 * 60 * 60

for i in range(c):
    cList.append(input())
    
for _ in range(c):
    hList.append(input())

intList = [] # 5 * 60*60 ~ 5*60*60 + 4






