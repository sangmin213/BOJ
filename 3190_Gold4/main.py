'''
implementation
'''

import sys
from collections import deque

def main():
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    
    mymap = [[0 for i in range(N)] for i in range(N)]
    body = [[[0,1] for i in range(N)] for i in range(N)] # [0,1] -> 0 : not my body in it , 1 : here direction is 1(=right)
    body[0][0] = [1,1]
    
    for _ in range(K):
        i,j = tuple(map(int, sys.stdin.readline().split()))
        mymap[i-1][j-1] = 1
    
    L = int(sys.stdin.readline())
    plan = deque([]) # moving plan
    for _ in range(L):
        moving = sys.stdin.readline().split() # ex. ('3', L)
        moving[0] = int(moving[0])
        plan.append(tuple(moving))
    
    eswn = 1 # initially 동쪽. 동 -> 남 -> 서 -> 북(R)
    head = [0,0]
    tail = [0,0]
    count = 0 # living time second
    TF = True
    
    while plan:
        myplan = plan.popleft() # tuple
        TF, eswn, count, head, tail, mymap, body = move(N, eswn, count, head, tail, mymap, body, myplan)
        if not TF:
            break
    
    # 더 이상의 plan이 없을 경우 현재 진행방향대로 직진
    if TF:
        myplan = (10000000000, 'D') # 끝까지 가라는 의미에서 10000000000번, 'D'는 형식상 맞춰줌
        TF, eswn, count, head, tail, mymap, body = move(N, eswn, count, head, tail, mymap, body, myplan)
    
    print(count)
    
    
def direction(key, eswn):
    if key == 'D':
        eswn += 1
    else:
        eswn -= 1
        
    if eswn < 0 :
        eswn += 4
    elif eswn >= 4:
        eswn -= 4
        
    return eswn


def sub_move(eswn):
    if eswn == 1: # right
        return (0, 1)
    elif eswn == 2: # down
        return (1, 0)
    elif eswn == 3: # left
        return (0, -1)
    elif eswn == 0: # up
        return (-1, 0)


def move(N, eswn, count, head, tail, mymap, body, myplan):
    total_move, next_direction = myplan
    
    for i in range(count, total_move):
        row, col = sub_move(eswn)
        # 끝나는 경우
        if head[0]+row < 0 or head[0]+row == N or head[1]+col < 0 or head[1]+col == N: # 벽에 부딪힌 경우
            return False, eswn, count+1, head, tail, mymap, body
        elif body[head[0]+row][head[1]+col][0] == 1: # 내 몸과 부딪힌 경우
            return False, eswn, count+1, head, tail, mymap, body
        
        head = [head[0]+row, head[1]+col] # head 위치 갱신
        # 사과를 먹은 경우
        if mymap[head[0]][head[1]] == 1:
            mymap[head[0]][head[1]] = 0 # 사과 없애기
        # 사과 안 먹은 경우
        elif mymap[head[0]][head[1]] != 1:
            row, col = sub_move(body[tail[0]][tail[1]][1])
            body[tail[0]][tail[1]] = [0,1] # body의 tail 현 위치 0으로 바꾸기
            tail = [tail[0]+row, tail[1]+col] # tail 위치 갱신
        
        # body에 head 위치 표기
        body[head[0]][head[1]] = [1, eswn]
    
        # count + 1
        count += 1
    
    # eswn 갱신
    eswn = direction(next_direction, eswn)
    # 갱신된 eswn으로 body의 head 위치 변경
    body[head[0]][head[1]] = [1, eswn]
    
    return True, eswn, count, head, tail, mymap, body
        

if __name__ == '__main__':
    main()