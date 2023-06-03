house = []
max_dist, N, C = 0, 0, 0

def DP(router, prev_small_move, direction):
    '''
    Args:
        - prev_small_move : 이전 가장 작은 거리를 지닌 두 라우터 중 움직인 라우터
        - direction : 위 라우터가 왼쪽(-1) 오른쪽(+1) 중 어디로 움직였는지
    '''
    global max_dist
    # find smallest
    local_small = 1e10
    small_idxes = []
    ''' get local small '''
    for idx in range(C-1):
        tmp = house[router[idx+1]] - house[router[idx]]
        if tmp < local_small:
            local_small = tmp
            small_idxes = [idx]
        elif tmp == local_small:
            small_idxes.append(idx)
    ''' compare max nearest distance '''
    if max_dist <= local_small:
        max_dist = local_small 
    else: return
    ''' change router '''
    for small_idx in small_idxes:
        if small_idx == 0:
            if prev_small_move == 1:
                return
            else:
                prev_small_move, direction = 1, 1
                router[1] += 1
                if router[1] > N-1:
                    return
        elif small_idx == C-2:
            if prev_small_move == C-2:
                return
            else:
                prev_small_move, direction = C-2, -1
                router[C-2] -= 1
                if router[C-2] < 0:
                    return
        else:
            if house[router[small_idx+2]] - house[router[small_idx+1]] > house[router[small_idx]] - house[router[small_idx-1]]:
                if prev_small_move == small_idx+1 and direction == -1:
                    return
                else:
                    prev_small_move, direction = small_idx+1, 1
                    router[small_idx+1] += 1
            else:
                if prev_small_move == small_idx and direction == 1:
                    return
                else:
                    prev_small_move, direction = small_idx, -1
                    router[small_idx] -= 1
        DP(router[:], prev_small_move, direction)


def main():
    global N, C, max_dist
    N, C = map(int, input().split())
    dist = N//C
    for i in range(N):
        house.append(int(input()))
    house.sort()
    router = [i for i in range(0,dist*(C-1),dist)]
    router.append(N-1)
    
    DP(router, -1, 0)
    print(max_dist)

    return

if __name__ == '__main__':
    main()