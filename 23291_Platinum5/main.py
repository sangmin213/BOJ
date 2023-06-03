from copy import deepcopy

def main():    
    N, K = tuple(map(int, input().split()))
    array = list(map(int, input().split()))
    cnt = 0
    while True:
        mini = min(array)
        maxi = max(array)
        if maxi - mini <= K:
            break
        for idx, val in enumerate(array):
            if val == mini:
                array[idx] += 1
        array = clean(array)
        cnt += 1
    
    print(cnt)
    

def spread(penthouse,res):
    h, w = len(penthouse), len(penthouse[0])
    
    pent_pm = [[0 for i in range(w)] for j in range(h)]
    res_pm = [0 for _ in res]
    # 층 있는 어항들
    for i in range(h-1):
        for j in range(w-1):
            tmp_w = penthouse[i][j] - penthouse[i][j+1] if penthouse[i][j] > penthouse[i][j+1] else penthouse[i][j+1] - penthouse[i][j]
            tmp_h = penthouse[i][j] - penthouse[i+1][j] if penthouse[i][j] > penthouse[i+1][j] else penthouse[i+1][j] - penthouse[i][j]
            if penthouse[i][j] > penthouse[i][j+1]:
                pent_pm[i][j] -= tmp_w//5
                pent_pm[i][j+1] += tmp_w//5
            else:
                pent_pm[i][j] += tmp_w//5
                pent_pm[i][j+1] -= tmp_w//5
            if penthouse[i][j] > penthouse[i+1][j]:
                pent_pm[i][j] -= tmp_h//5
                pent_pm[i+1][j] += tmp_h//5
            else:
                pent_pm[i][j] += tmp_h//5
                pent_pm[i+1][j] -= tmp_h//5
    # 맨 아래층 컬럼 간 계산해주기
    for j in range(w-1):
        if penthouse[-1][j] > penthouse[-1][j+1] :
            pent_pm[-1][j] -= (penthouse[-1][j] - penthouse[-1][j+1])//5
            pent_pm[-1][j+1] += (penthouse[-1][j] - penthouse[-1][j+1])//5
        else:
            pent_pm[-1][j] += (penthouse[-1][j+1] - penthouse[-1][j])//5
            pent_pm[-1][j+1] -= (penthouse[-1][j+1] - penthouse[-1][j])//5
    # 맨 우측열 행 간 계산해주기
    for i in range(h-1):
        if penthouse[i][-1] > penthouse[i+1][-1]:
            pent_pm[i][-1] -= (penthouse[i][-1] - penthouse[i+1][-1])//5
            pent_pm[i+1][-1] += (penthouse[i][-1] - penthouse[i+1][-1])//5
        else:
            pent_pm[i][-1] += (penthouse[i+1][-1] - penthouse[i][-1])//5
            pent_pm[i+1][-1] -= (penthouse[i+1][-1] - penthouse[i][-1])//5
                
    if len(res):
        # 층 없는 꼬리 어항들
        for i in range(len(res)-1):
            if res[i] > res[i+1] :
                res_pm[i] -= (res[i]-res[i+1])//5
                res_pm[i+1] += (res[i]-res[i+1])//5
            else :
                res_pm[i] += (res[i+1]-res[i])//5
                res_pm[i+1] -= (res[i+1]-res[i])//5
        # 꼬리 어항과 층 있는 어항의 연결점
        if res[0] > penthouse[-1][-1]:
            res_pm[0] -= (res[0] - penthouse[-1][-1])//5
            pent_pm[-1][-1] += (res[0] - penthouse[-1][-1])//5
        else:
            res_pm[0] += (penthouse[-1][-1] - res[0])//5
            pent_pm[-1][-1] -= (penthouse[-1][-1] - res[0])//5
        # plus minus
        for i, val in enumerate(res_pm):
            res[i] += val
    
    # plus minus
    for i in range(h):
        for j in range(w):
            penthouse[i][j] += pent_pm[i][j]
    
    # 한 줄로 다시 맞추기
    result = []
    for col in list(zip(*penthouse)):
        for i in reversed(list(col)):
            result.append(i)
    result += res
    
    return result

rotate90 = lambda x : [list(ll) for ll in list(zip(*reversed(x)))]
def clean(array):
    ''' rotate90 '''
    # 0 1(-1) 2(-2) 2(-4) 3(-6) 3(-9) 4(-12) 4(-16) 5(-20) 5(-25)
    length = len(array)
    cnt = 4
    res = deepcopy(array[2:]) # 위에 층이 쌓이지 않은 어항들
    penthouse = [[ array[0] ], [ array[1] ]]
    while True:
        need_res = cnt//2 # 1층에 남아있어야 할 최소 어항 수
        used = need_res ** 2 if cnt % 2 else need_res * (need_res - 1) # 위 층에 올라갈 어항 수 (홀짝) = 펜트하우스 수
        if length - used < need_res:
            break
        # rotation에 array[used : used+need_res]가 append되어야함.
        penthouse = rotate90(penthouse)
        penthouse.append(res[:need_res])
        res = res[need_res:]
        cnt+=1  
    ''' spread '''
    new_array = spread(penthouse, res)    

    ''' rotate180 '''
    penthouse = [new_array[:length//2]]
    res = new_array[length//2:]
    
    penthouse = rotate90(rotate90(penthouse)) # n//2
    penthouse = rotate90(rotate90([res[:length//4]])) + rotate90(rotate90([penthouse[0][:length//4]])) + [penthouse[0][length//4:]] + [res[length//4:]] # n//4
    ''' spread '''
    new_array = spread(penthouse, [])
    
    return new_array

if __name__ == '__main__':
    main()