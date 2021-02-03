from collections import deque
import copy
mini=999999

def find_path(si,sj,ei,ej,board):
    queue=deque()
    queue.append((si,sj,0))
    visited=[[0]*4 for _ in range(4)]
    while queue:
        i,j,count=queue.popleft()
        if i==ei and j==ej:
            return count
        for direction in ('U','D','L','R'):#Ctrl 이동
            if direction=='U':
                i_copy=i
                while (0<i_copy and not board[i_copy][j]) or i_copy==3:
                    i_copy-=1
                if i_copy!=i:
                    queue.append((i_copy,j,count+1))
            elif direction=='D':
                i_copy=i
                while (i_copy<3 and not board[i_copy][j]) or i_copy==0:
                    i_copy+=1
                if i_copy!=i:
                    queue.append((i_copy,j,count+1))
            elif direction=='L':
                j_copy=j
                while (0<j_copy and not board[i][j_copy]) or j_copy==3:
                    j_copy-=1
                if j_copy!=j:
                    queue.append((i,j_copy,count+1))
            else:
                j_copy=j
                while (j_copy<3 and not board[i][j_copy]) or j_copy==0:
                    j_copy+=1
                if j_copy!=j:
                    queue.append((i,j_copy,count+1))
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)): #그냥 이동
            if 0<=i+di<4 and 0<=j+dj<4 : #방문하지 않았다면
                queue.append((i+di,j+dj,count+1))
        

def bfs(card,r,c,board):
    global mini
    queue=deque()
    queue.append((0,card,r,c,0,board))
    while queue:
        state,cards,i,j,count,board=queue.popleft()
        if mini<count:
            continue
        if state: #Enter
            for index,card in enumerate(cards):
                if state==card[0]:
                    board_copy=copy.deepcopy(board)
                    board_copy[i][j]=0
                    queue.append((0,cards[:index]+cards[index+1:],card[1][0],card[1][1],count+find_path(i,j,card[1][0],card[1][1],board_copy)+1,board_copy))
            
        else: #Enter가 눌리지 않은상태
            if not cards: #카드가 없다면
                if mini>count:
                    mini=count
                    continue
            for index,card in enumerate(cards):
                board_copy=copy.deepcopy(board)
                board_copy[i][j]=0
                queue.append((card[0],cards[:index]+cards[index+1:],card[1][0],card[1][1],count+find_path(i,j,card[1][0],card[1][1],board_copy)+1,board_copy))
            
def solution(board, r, c):
    answer = 0
    card=[]
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                card.append([board[i][j],(i,j)])
    card.sort()
    bfs(card,r,c,board)
    return mini

'''
굉장히 오랫동안 구현한 문제..
testcase 25번만 실패함.. 왜실패하는지 잘모르겠음 ㅠㅠ
'''