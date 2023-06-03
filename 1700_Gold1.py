def plugInOut(onMultitab, removable, elec, item):
    rm = removable.pop()
    onMultitab.remove(rm)
    onMultitab.append(item)
    elec[rm] = 0
    elec[item] = 1


def main():
    N, K = map(int,input().split())
    order = list(map(int,input().split()))

    onMultitab, removable = [], []
    elec = [0 for i in range(K+1)]
    cnt, plug_out = 0, 0
    for i, item in enumerate(order):
        if elec[item] == 1: # 이미 사용 중인 기기의 경우 패스
            continue
        elif cnt < N: # 멀티탭에 자리 있는 경우 사용
            onMultitab.append(item)
            elec[item] = 1
            cnt+=1
        elif len(removable): # 새로운 기기 사용을 위해 제거할 기기 찾기
            plugInOut(onMultitab, removable, elec, item)
            plug_out += 1
        else:
            tmp = onMultitab[:]
            rm = N
            for nxt in order[i+1:]: 
                if rm == 1: # 마지막 하나 남은 경우
                    break
                if elec[nxt] == 1:
                    try: 
                        tmp.remove(nxt)
                        rm -= 1
                    except: continue
            removable += tmp
            plugInOut(onMultitab, removable, elec, item)
            plug_out += 1
            
    print(plug_out)
    return

if __name__ == '__main__':
    main()