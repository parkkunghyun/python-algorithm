import sys

read = sys.stdin.readline

T = int(read())
for _ in range(T):
    N = int(read())
    finish = list(map(int, read().split()))
    teams = max(finish)
    # team의 멤버 일단 6명인지 체크하기
    teams_1 = dict()
    for t in range(1, teams+1):
        members = 0
        for person in finish:
            if t == person:
                members+=1
        if members == 6:
            teams_1[t] = 0
    # team_1의 점수 구하기 및 정렬하기 -> 그 중 4명!
    for team in teams_1.keys():
        c = 1
        mc = 0
        for i in range(len(finish)):
            if finish[i] in teams_1:
                if team == finish[i] and mc < 4:
                    teams_1[team] += c
                    mc += 1
                c += 1
    sorted_teams = sorted(teams_1.items(), key= lambda x : x[1])
    # 동점인 경우 5번째 멤버의 점수 확인하기
    same_teams = []
    minScore = sorted_teams[0][1]
    for k,v in sorted_teams:
        if minScore == v:
            same_teams.append(k)
    # 아제 동점 체크해주기!
    if len(same_teams) == 1:
        print(same_teams[0])
    else:
        result = 0
        result_teams =  dict()
        for team in same_teams:
            result_teams[team] = 0
            c = 1
            mc = 0
            for i in range(len(finish)):
                if finish[i] in same_teams:
                    if team == finish[i]:
                        if mc ==4: 
                            result_teams[team] += c
                        mc += 1
                    c += 1
        result = sorted(result_teams.items(), key= lambda x : x[1])
        print(result[0][0])



    