from collections import deque
from copy import deepcopy

def find_far(defense):
    for i, row in enumerate(defense):
        if sum(row)!=0:   return i

def bfs(x,y, M,D, defense):
    dist = 1
    queue = deque([(x,y,dist)])
    visited = [[0 for i in range(len(defense[0]))] for j in range(len(defense))]
    dx, dy = [0,-1,0], [-1,0,1] # left-first
    enemy = False

    while queue:
        x, y, dist = queue.popleft()
        visited[x][y] = 1
        if defense[x][y] == 1:
            enemy = True
            break
        for ddx, ddy in zip(dx,dy):
            if 0 <= x+ddx and 0 <= y+ddy < M:
                if not visited[x+ddx][y+ddy] and dist < D:
                    queue.append((x+ddx, y+ddy, dist+1))
                
    return enemy, x, y

def enemy_access(defense, M):
    for i in range(len(defense)-1, 0, -1):
        defense[i] = defense[i-1]
    defense[0] = [0] * M # 없어도 됨. defense[1]과 defense[0]이 같은 객체를 reference 하고 있고, defense[1]부터 공격할 것이기 때문.

def game(i,j,k, n,N,M,D, defense):
    result = 0
    while n < N:
        # find enemy
        tmp_list = []
        tmp_list.append(bfs(N-1, i, M,D, defense))
        tmp_list.append(bfs(N-1, j, M,D, defense))
        tmp_list.append(bfs(N-1, k, M,D, defense))
        
        # kill
        prev_x, prev_y = -1, -1
        for enemy, x, y in tmp_list:
            if enemy and (x != prev_x or y != prev_y):
                result += 1
                defense[x][y] = 0
                prev_x, prev_y = x, y # find enemy도 left to right 이므로 이렇게만 바꿔줘도 충분함.

        # next turn
        enemy_access(defense, M)
        
        n+=1

    return result

def main():
    N, M, D = map(int, input().split())
    defense = [list(map(int, input().split())) for _ in range(N)] # defense map
    result = 0
    n = find_far(defense) # find farthest enemy
    for i in range(M-2):
        for j in range(i+1,M-1):
            for k in range(j+1,M):
                result = max(result, game(i,j,k, n,N,M,D, deepcopy(defense)))

    print(result)
    return

if __name__ == '__main__':
    main()