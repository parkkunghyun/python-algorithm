"""

1. set으로 중복 안되는 이름만 저장
2. vistied라는 딕셔너리를 만들어서 방문 확인
3. 
"""
n, game = input().split()
print(n, game)
all = []
persons = set()
for _ in range(int(n)):
    person = input()
    all.append(person)
    persons.add(person)

persons = list(persons)
# print(all)
# print(persons)

visited = {}
for p in persons:
    if p not in visited:
        visited[p] = False
#print(visited)

answer = 0
check = 0
if game == 'Y':
    answer = len(persons)
elif game == 'F':
    for p in all:
        if visited[p] == False:
            check += 1
            visited[p] = True
        if check == 2:
            answer += 1
            check = 0
    if check == 2:
        answer += 1
else:
    for p in all:
        if visited[p] == False:
            check += 1
            visited[p] = True
        if check == 3:
            answer += 1
            check = 0
    if check == 3:
        answer += 1

print(answer)