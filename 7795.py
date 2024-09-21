"""
각각을 입력받고
A와 B의 쌍을 구하기

2만개 * 2만개 => 시간 초과
A는 낮은 순으로 정렬하기
B는 높은 순으로 정렬하기

만약 A현재 애가 B 높은애보다 낮으면 바로 멈추기

"""
import sys
read = sys.stdin.readline


def check(aList, bList):
    #print(f'aList -> {aList}')
    #print(f'bList -> {bList}')
    answer = 0 
    for a in aList:
        for b in bList:
            if a > b:
                #print(f'{a} -> {b}')
                answer+= 1
            else:
                break
    return answer


T = int(read())

for _ in range(T):
    A,B = map(int,read().split())
    aList = list(map(int, read().split()))
    bList = list(map(int, read().split()))
    aList.sort(reverse=True)
    bList.sort()
    answer = check(aList, bList)
    print(answer)