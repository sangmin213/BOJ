'''
direction이 주어지면 그 방향으로 벽에 도달 / 출구에 도달할 때 까지 움직인다.
벽에 도달한 경우, 나머지 방향들로 움직여 본다. 이를 dfs로 구현한다.
- 이전에 방문한 적이 있는 경우 pass
- 방문한 적이 없는 경우 이동.
- direction_change가 10번이 넘어가면 종료
- out에 도달하면 종료 / 이 때 blue도 out에 도달가능한지 확인 필요
'''

import sys
from copy import deepcopy


def submove(direction):
    if direction == 0:
        return 0, 1
    elif direction == 1:
        return 0, -1
    elif direction == 2:
        return -1, 0
    else:
        return 1, 0
    
def move_order(direction, red_cur, blue_cur):
    # 빨간 구슬을 먼저 움직이는 경우:
    # # 오른쪽으로 움직일 건데 빨간 구슬이 더 오른쪽에 위치해있는 경우
    # # 왼쪽으로 움직일건데 빨간 구슬이 더 왼쪽에 위치한 경우
    # # 위로 움직일 건데 빨간 구슬이 더 위에 있는 경우
    # # 아래로 움직일 건데 빨간 구슬이 더 아래에 있는 경우
    if direction == 0 and red_cur[1] > blue_cur[1]:
        return 1 # 빨간 구슬 먼저
    elif direction == 1 and red_cur[1] < blue_cur[1]:
        return 1
    elif direction == 2 and red_cur[0] < blue_cur[0]:
        return 1
    elif direction == 3 and red_cur[0] > blue_cur[0]:
        return 1
    else:
        return 0
    

def dfs(direction, direction_change, roadmap, red_cur, blue_cur):
    result = -1
    
    # 10번 넘게 움직인 경우
    if direction_change > 10:
        return -1
    
    row_dir, col_dir = submove(direction)

    # 빨간 구슬, 파란 구슬 이동
    order = move_order(direction, red_cur, blue_cur)
    if order == 1:
        while roadmap[red_cur[0]+row_dir][red_cur[1]+col_dir] == '.':
            roadmap[red_cur[0]][red_cur[1]] = '.' # roadmap 갱신
            red_cur = [red_cur[0] + row_dir, red_cur[1] + col_dir]
            roadmap[red_cur[0]][red_cur[1]] = 'R' # roadmap 갱신
        while roadmap[blue_cur[0]+row_dir][blue_cur[1]+col_dir] == '.':
            roadmap[blue_cur[0]][blue_cur[1]] = '.' # roadmap 갱신
            blue_cur = [blue_cur[0] + row_dir, blue_cur[1] + col_dir]
            roadmap[blue_cur[0]][blue_cur[1]] = 'B' # roadmap 갱신
    else:
        while roadmap[blue_cur[0]+row_dir][blue_cur[1]+col_dir] == '.':
            roadmap[blue_cur[0]][blue_cur[1]] = '.' # roadmap 갱신
            blue_cur = [blue_cur[0] + row_dir, blue_cur[1] + col_dir]
            roadmap[blue_cur[0]][blue_cur[1]] = 'B' # roadmap 갱신
        while roadmap[red_cur[0]+row_dir][red_cur[1]+col_dir] =='.':
            roadmap[red_cur[0]][red_cur[1]] = '.' # roadmap 갱신
            red_cur = [red_cur[0] + row_dir, red_cur[1] + col_dir]
            roadmap[red_cur[0]][red_cur[1]] = 'R' # roadmap 갱신
            
    
    # 파란 구슬이 탈출한 경우
    if roadmap[blue_cur[0]+row_dir][blue_cur[1]+col_dir] == 'O':
        return -1
    
    # 빨간 구슬이 탈출한 경우
    elif roadmap[red_cur[0]+row_dir][red_cur[1]+col_dir] == 'O':
        # 파란 구슬이 바로 뒤에 위치한 경우 == 같이 탈출하게 되는 경우
        if blue_cur[0] + row_dir == red_cur[0] and blue_cur[1] + col_dir == red_cur[1] :
            return -1
        # 빨간 구슬만 탈출한 경우
        return direction_change
    
    # 계속 해야함
    else:
        # 불필요한 움직임 제거 == 위로 갔는데 바로 다음 차례에 아래로 내려가는 일 없도록 함.
        if direction < 2: range_ = [2,3]
        else: range_ = [0,1]
        for i in range_:
            tmp = dfs(i, direction_change + 1, deepcopy(roadmap), red_cur, blue_cur)
            if tmp != -1:
                if result == -1:
                    result = tmp
                else:
                    if result > tmp:
                        result = tmp
    
    return result
    

def main():
    N, M = tuple(map(int, sys.stdin.readline().split()))
    
    roadmap = []
    for _ in range(N):
        string = sys.stdin.readline().split()[0]
        roadmap.append([s for s in string])
    
    for i in range(N):
        for j in range(M):
            if roadmap[i][j] == 'R':
                red_cur = [i,j]
            elif roadmap[i][j] == 'B':
                blue_cur = [i,j]
    
    direction_change = 1
    direction = 0 # 0: right, 1: left, 2: up, 3: down
    
    result = -1
    for direction in range(4):
        tmp = dfs(direction, direction_change, deepcopy(roadmap), red_cur, blue_cur)
        if tmp != -1:
            if result == -1:
                result = tmp
            else:
                if result > tmp:
                    result = tmp
    
    print(result)
    
if __name__ == '__main__':
    main()