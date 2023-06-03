def main():
    N = int(input())
    graph = {}
    desk = [[0 for i in range(N)] for j in range(N)]

    for i in range(N*N):
        tmp = list(map(int, input().split()))
        graph[tmp[0]] = tmp[1:]
    
    desk[1][1] = list(graph.keys())[0]
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    for key in list(graph.keys())[1:]:
        neighbor, blank, rr, cc =  0, 0, 0, 0
        for i, row in enumerate(desk):
            for j, pos in enumerate(row):
                if pos != 0:
                    continue
                tmp_neighbor = 0
                tmp_blank = 0
                for ddx, ddy in zip(dx, dy):
                    if 0 <= i+ddx < N and 0 <= j+ddy < N:
                        if desk[i+ddx][j+ddy] == 0 : tmp_blank += 1
                        elif desk[i+ddx][j+ddy] in graph[key]:  tmp_neighbor += 1
                if tmp_neighbor < neighbor: 
                    continue
                elif tmp_neighbor > neighbor:
                    neighbor, blank, rr, cc = tmp_neighbor, tmp_blank, i, j
                else:
                    if blank > tmp_blank:   continue
                    elif blank < tmp_blank:
                        blank, rr, cc = tmp_blank, i, j

        desk[rr][cc] = key

    result = 0
    for i in range(N):
        for j in range(N):
            key = desk[i][j]
            cnt = 0
            for ddx, ddy in zip(dx, dy):
                if 0 <= i+ddx < N and 0 <= j+ddy < N:
                    if desk[i+ddx][j+ddy] in graph[key]:    cnt += 1
            if cnt != 0:
                result += 10**(cnt-1)
    print(result)

    return

if __name__ == '__main__':
    main()