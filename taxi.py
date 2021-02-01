처음 풀이

import heapq
INF = 200*100000
def solution(n, s, a, b, fares):
    global graph
    answer = 0
    graph=[[] for _ in range(n+1)]
    for start,end,cost in fares: 
        graph[start].append((end,cost))
        graph[end].append((start,cost))
    result=[[]]
    for i in range(1,n+1): 
        result.append(dijkstra([INF]*(n+1),i))
    mini=result[s][a]+result[s][b]
    for i in range(1,n+1): 
        if result[s][i]+result[i][a]+result[i][b] < mini:
            mini=result[s][i]+result[i][a]+result[i][b]
    return mini

def dijkstra(visited,s):
    global graph
    queue=[]
    visited[s]=0
    queue.append((0,s))
    while queue:
        dist,node=heapq.heappop(queue)
        if dist > visited[node]:
            continue
        for i in graph[node]:
            cost=i[1]+dist
            if cost < visited[i[0]]:
                visited[i[0]]=cost
                queue.append((cost,i[0]))
    return visited

처음풀이 에서 7,8번이 자꾸 시간초과가 나옴 그래서 floyd washall을 floyd알고리즘을 노드의 개수만큼 더 반복한 방법보다, 더 쉬운방법이 있다는 것을 알게됨.
n**3번 돌면서, 각정점에대해서 이정점을 거치는것과 그냥가는것에대해서 초기화를 해주면된다.

2번째 풀이
import heapq
INF = 200*100000
def solution(n, s, a, b, fares):
    global graph
    answer = 0
    graph=[[INF]*(n+1) for _ in range(n+1)]
    for start,end,cost in fares: 
        graph[start][end]=cost
        graph[end][start]=cost
    for path in range(1,n+1):
        for start in range(1,n+1):
            for end in range(1,n+1):
                if start==end:
                    graph[start][end]=0
                elif graph[start][end] > graph[start][path]+graph[path][end]:
                    graph[start][end]=graph[start][path]+graph[path][end]
    mini=graph[s][a]+graph[s][b]
    for i in range(1,n+1):
        if mini > graph[s][i]+graph[i][a]+graph[i][b]:
            mini=graph[s][i]+graph[i][a]+graph[i][b]
    return mini

성공!

알게된점 : floyd washall을 dijkstra를 n번 더 하는것보다 더쉽게 구할수 있는 방법!!
