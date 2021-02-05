#처음풀이
from itertools import permutations

def solution(n, k):
    return list(permutations([i for i in range(1,n+1)],n))[k-1]

'''
문제를 자세히 안읽는 습관이 있는것 같다. 덥석 idea가 떠올라서 단순히 permutation을 한 후에, 해당 원소값을 가져오는것으로 했지만, 생각해보니 시간복잡도는 20!까지 가게되서, 시간초과가 불가피하다. 따라서 무언가 logic을 바꿀 필요를 느꼈다.
'''

#두번째 풀이
def solution(n, k):
    k-=1
    answer = []
    num=[a for a in range(1,n+1)]
    temp=1
    for a in range(1,n+1):
        temp*=a
    goal=n
    while len(answer)<goal:
        start,index=0,1
        temp/=n #n-1!
        end=temp
        for i in num:
            if start<=k<end:
                k-=start
                index=i
                break
            else:
                start=end
                end+=temp
        answer.append(index)
        num.remove(index)
        n-=1
    return answer

'''일단 permutations을 못쓰니, 직접 위치를 구해야 겠다 생각해서, 그림을 그려가며 이해하려고 노력해보았고, 그에 상응하는 코딩을 하여서 해결되었다.
'''