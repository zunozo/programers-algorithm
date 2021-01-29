https://programmers.co.kr/learn/courses/30/lessons/72412

순위검색

import re
def solution(info, query):
    answer = [0 for _ in range(len(query))]
    for i in range(len(query)):
        query[i]=re.split(' and | ',query[i])
    for i in range(len(info)):
        info[i]=info[i].split()
        for q in range(len(query)):
            if (query[q][0]=='-' or query[q][0]==info[i][0]) and (query[q][1]=='-' or query[q][1]==info[i][1]) and (query[q][2]=='-' or query[q][2]==info[i][2]) and (query[q][3]=='-'or query[q][3]==info[i][3]) and (int(query[q][4]) <= int(info[i][4])):
                answer[q]+=1
    return answer

안풀려서 kakaotech 해설 참고..
나중에 다시풀어보자(안풀림.)