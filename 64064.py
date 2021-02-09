#처음풀이
from itertools import product

def solution(user_id, banned_id):
    answer = []
    candidate_id=[[] for _ in range(len(banned_id))]
    for idx,ban in enumerate(banned_id):
        for user in user_id:
            if len(ban)==len(user):
                for i in range(len(user)):
                    if ban[i]!=user[i] and ban[i]!='*':
                        break
                else:
                    #가능한 user_id
                    candidate_id[idx].append(user)
    print(candidate_id)
    result=list(product(*candidate_id))
    for i in range(len(result)):
        if len(set(result[i])) == len(result[i]):
            answer.append(tuple(sorted(set(result[i]))))
    print(set(answer))
    return len(set(answer))
    
'''너무 카티션 프로덕트를 이용하려고해서그런가.. testcase5번이 자꾸 시간초과한다. 이유를 모르겠어서, 다른방식으로 푼것을 참고하였다..

다른분의 풀이
'''
from itertools import permutations

def isMatch(user_set, banned_set):
    for i in range(len(user_set)):
        if len(user_set[i])!=len(banned_set[i]):
            return False
        for j in range(len(user_set[i])):
            if banned_set[i][j]=='*':
                continue
            if user_set[i][j]!=banned_set[i][j]:
                return False
    return True
    
def solution(user_id, banned_id):
    ans=[]
    for com_set in permutations(user_id, len(banned_id)):
        if isMatch(com_set, banned_id):
            com_set = set(com_set) # 중복 제거
            if com_set not in ans:
                ans.append(com_set)
    return len(ans)

'''
흐름:
permutations으로 모든 가능한 경우의수를 체크하였다.
체크하는 함수에서는 길이와 문자가 *가아닌데 다르다면 false를 return하는 형식으로 체크하였다.
만약 True라면, 중복을 set으로 제거하여 정답list에 없으면 append해준다.
느낀점
더 직관적인 풀이같다.


알게된점
*의 활용
함수에 가변적인 인수중 list를 넘겨주고싶다면,
ex) product(*candidate_id)
함수에 가변적인 인수중 dict를 넘겨주고싶다면,
ex) product(**candidate_id) 
오류
TypeError: unhashable type: 'list'
set에는 바뀔수있는 것들이 들어갈수없다.
따라서, list는 tuple로 등등 바꿔줘야한다.
'''