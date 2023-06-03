'''
           32 (final)
(start)    20
1             19
2          26    18
3                   17
4          25         16
5 21 22 23 24 31 30 29  15
 6                    14
    7      28       13
      8          12
        9  27 11
           10

'''

from copy import deepcopy

red_goto_map = [i for i in range(1, 21)] + [32] + [i for i in range(22, 27)] + [20] + [28, 24] + [30, 31, 24] + [-1]
blue_goto_map = deepcopy(red_goto_map)
blue_goto_map[5], blue_goto_map[10], blue_goto_map[15] = 21, 27, 29
score_map = [2*i for i in range(21)] + [13, 16, 19, 25, 30, 35, 22, 24, 28, 27, 26, 0]


def make_mal(tmp):
    mal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cnt = 0
    while True:            
        mal[cnt] = tmp % 4
        tmp //= 4
        if tmp == 0:
            break
        cnt += 1
    return mal


def main():
    yout = list(map(int, input().split()))
    all_case_result = [0 for i in range(4**10)]

    # 4진수
    for i in range(4**10):
        mal_loc = [0,0,0,0]
        mals = make_mal(i)

        exit_flag = 0
        score = 0
        for idx, mal in enumerate(mals):
            if mal_loc[mal] == -1 : # 이미 말이 난 경우 : 난 말을 또 하는 경우는 없으므로 이번 경우의 수 아예 삭제
                score = 0
                break
            for yy in range(yout[idx]): # 이번 주사위 윷 값만큼 이동
                if yy == 0: # 본 위치에서 이동 시작 = blue 고려
                    if yy == yout[idx] - 1: # yout=1, 즉 한 칸만 움직이는 경우
                        if blue_goto_map[mal_loc[mal]] in mal_loc:
                            exit_flag = 1
                            break
                    mal_loc[mal] = blue_goto_map[mal_loc[mal]]
                elif yy == yout[idx] - 1: # 종착지에 다른 말이 있는지 검사
                    if red_goto_map[mal_loc[mal]] in mal_loc:
                        exit_flag = 1
                        break
                    mal_loc[mal] = red_goto_map[mal_loc[mal]]
                else:
                    mal_loc[mal] = red_goto_map[mal_loc[mal]] # red direction
                if mal_loc[mal] == 32: # 말이 도착 지점에 도착한 경우
                    mal_loc[mal] = -1
                    break
            if exit_flag:
                score = 0
                break
            score += score_map[mal_loc[mal]]
        
        all_case_result[i] = score            
        
    result = max(all_case_result)
    print(result)

    return


if __name__ == '__main__':
    main()