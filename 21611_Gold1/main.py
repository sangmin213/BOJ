'''
implementation
math
'''
from copy import deepcopy

def main():
    N, M = tuple(map(int,input().split()))
    
    tmp_marble = []
    for n in range(N):
        tmp_marble.append(list(map(int,input().split())))
        
    blizzard = [] # 1,2,3,4 : U(+6),D(+2),L,R(+4)
    for m in range(M):
        blizzard.append(tuple(map(int,input().split())))
        
    marble = get_marble(tmp_marble)
    
    magic(marble, blizzard, N*N)
    
    
def get_marble(tmp_marble):
    marble = []
    
    N = len(tmp_marble[0])
    visit = [[0 for i in range(N)] for j in range(N)]
    i, j = 0,0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    d = 0
    cnt = 0
    
    while cnt < N*N:
        marble.append(tmp_marble[i][j])
        visit[i][j] = 1
        
        if i+dx[d] == N or i+dx[d] < 0 or j+dy[d] == N or j+dy[d] < 0 or visit[i+dx[d]][j+dy[d]] == 1:
            d = (d+1)%4
        
        i += dx[d]
        j += dy[d]
        cnt += 1
    
    return list(reversed(marble))
    
    
def magic(marble, blizzard, length):
    '''
    왼쪽으로 쏠 경우 : 첫 번째 왼쪽 칸: 1번 인덱스, 두 번째 왼쪽 칸: (3*4-4+1)번 인덱스, ...
    아래쪽으로 쏠 경우 : 첫 번째 왼쪽 칸: 1+2번 인덱스, 두 번째 왼쪽 칸: (3*4-4+1)+2번 인덱스
    오른쪽으로 쏠 경우 : 첫 번째 왼쪽 칸: 1+4번 인덱스, 두 번째 왼쪽 칸: (3*4-4+1)+4번 인덱스
    위쪽으로 쏠 경우 : 첫 번째 왼쪽 칸: 1+6번 인덱스, 두 번째 왼쪽 칸: (3*4-4+1)+6번 인덱스
    '''
    marble_bomb = [0,0,0,0]
    # blizard !!!
    for (d, s) in blizzard: # direction, size
        bl = 0
        if d==1:
            for ss in range(s):
                bl += (2*ss+1) * 4 - 4 + 1 + 6
                marble[bl] = 0
        elif d==2:
            for ss in range(s):
                bl += (2*ss+1) * 4 - 4 + 1 + 2
                marble[bl] = 0
        elif d==3:
            for ss in range(s):
                bl += (2*ss+1) * 4 - 4 + 1
                marble[bl] = 0
        elif d==4:
            for ss in range(s):
                bl += (2*ss+1) * 4 - 4 + 1 + 4
                marble[bl] = 0
        
        # marble pop !
        prev_marble = deepcopy(marble)
        while True:
            cnt = 0
            cur = 0
            zero_cnt = 0
            for idx, item in enumerate(marble):
                if item == 0:
                    zero_cnt += 1
                    continue
                if cur == 0:
                    cur = item
                    cnt += 1
                elif cur == item:
                    cnt += 1
                elif cur != item:
                    if cnt >= 4:
                        marble[idx-(cnt+zero_cnt) : idx] = [0 for _ in range(zero_cnt+cnt)]
                        marble_bomb[cur] += cnt
                    cnt = 1
                    cur = item
                    zero_cnt = 0
            
            if prev_marble == marble:
                break
            prev_marble = deepcopy(marble)
            
        # 연속 구슬로 끝나버린 경우
        if cnt >= 4:
            idx += 1
            marble[idx-(cnt+zero_cnt) : idx] = [0 for _ in range(zero_cnt+cnt)]
            marble_bomb[cur] += cnt
                
        # marble change!
        new_marble = [0 for _ in marble]
        cnt = 0
        cur = 0
        new_idx = 1 # 첫 번째 자리는 항상 0 (중심. 시작 위치)
        for idx,item in enumerate(marble):
            if item == 0:
                continue
            if cur == 0:
                cur = item
                cnt += 1
            elif cur == item:
                cnt += 1
            elif cur != item:
                if new_idx == length:
                    break
                new_marble[new_idx] = cnt
                new_marble[new_idx+1] = cur

                cnt = 1
                cur = item
                new_idx += 2
                
         # 같은 구슬 뿐이라서 입력이 안 된 경우: 끝까지 다 돌았고, 마지막 구슬 2개가 같거나 마지막 2개 중 하나가 0인 경우
        if idx == length-1 and (marble[idx]==marble[idx-1] or marble[idx]==0 or marble[idx-1]==0):
            if new_idx < length:
                new_marble[new_idx] = cnt
            if new_idx+1 < length:
                new_marble[new_idx+1] = cur
            
        marble = new_marble    
    
    result = 0
    for idx, item in enumerate(marble_bomb):
        result += idx*item
        
    print(result)
    
def show(marble):
    for idx,item in enumerate(marble):
        print(item, end=" ")
        if idx%9 == 8:
            print()
    print()
    
if __name__ == '__main__':
    main()

'''
9 1
0 0 0 0 0 0 0 0 0
3 2 1 3 1 3 3 3 0
1 3 3 3 1 3 3 1 0
0 2 2 2 1 2 2 1 0
0 1 2 1 0 2 2 1 0
0 3 3 1 1 2 2 2 0
0 3 3 3 1 1 1 2 0
0 1 1 1 3 3 3 2 0
0 0 0 0 0 0 0 0 0
1 3
'''