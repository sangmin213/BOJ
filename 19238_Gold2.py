from copy import deepcopy
from collections import deque

def bfs(sx, sy, F, visited, road, find, N):
    level = 0
    queue = deque([(sx, sy, level)])
    visited[sx][sy] = 1

    if road[sx][sy] == find: # 첫 출발점에 사람이 있는 경우
        road[sx][sy] = 0
        return sx, sy, F

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    rx, ry = N, N # result x, y 좌표
    while queue:
        tx, ty, tlevel = queue.popleft()
        visited[tx][ty] = 1
        # find = 2
        if find == 2:
            if level != 0 and tlevel > level: # 가장 가까운 승객을 찾은 경우
                break
            if road[tx][ty] != 0 and road[tx][ty][1] == find:
                if level == 0:
                    rx, ry, level = tx, ty, tlevel
                elif tlevel == level:
                    if tx < rx :    rx, ry = tx, ty
                    elif tx == rx:
                        if ty < ry: ry = ty
                continue
        # find = 3
        if find == 3:
            if road[tx][ty] != 0 and road[tx][ty][1] == find and road[sx][sy][0] == road[tx][ty][0]:
                rx, ry, level = tx, ty, tlevel
                break
        
        for ddx, ddy in zip(dx, dy):
            if 0 <= tx + ddx < N and 0 <= ty + ddy < N:
                if visited[tx+ddx][ty+ddy] == 0:
                    queue.append((tx+ddx, ty+ddy, tlevel+1))

    if find == 3:
        road[sx][sy], road[rx][ry] = 0, 0

    return rx, ry, level

def main():
    N, M, F = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(N)]
    visited = deepcopy(road)
    sx, sy = map(int, input().split())
    info = {}
    for m in range(M):
        sr, sc, dr, dc = map(int, input().split())
        road[sr-1][sc-1] = [m,2] # 승객
        road[dr-1][dc-1] = [m,3] # 목적지
    
    sx, sy = sx-1, sy-1
    for m in range(M):
        sx, sy, move = bfs(sx, sy, F, deepcopy(visited), road, 2, N)
        if sx == N or F - move < 0:
            print(-1)
            return
        F -= move

        sx, sy, move = bfs(sx, sy, F, deepcopy(visited), road, 3, N)
        if sx == N or F - move < 0:
            print(-1)
            return
        F += move

    print(F)

    return

if __name__ == '__main__':
    main()