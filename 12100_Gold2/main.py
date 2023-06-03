import sys

def main():
    N = int(sys.stdin.readline())
    map2048 = []
    
    for _ in range(N):
        map2048.append(list(map(int, sys.stdin.readline().split())))
        
    maximum = 0
    for i in range(1024):
        direction_list = [0,0,0,0,0] # 0: right, 1: left, 2: up, 3: down
        cnt = 0
        while True:
            direction_list[cnt] = i%4
            i //= 4
            if not i:
                break
            cnt += 1
        tmp_result = play(direction_list, map2048)
        if maximum < tmp_result:
            maximum = tmp_result
    
    print(maximum)
    

def play(direction_list, map2048):
    for direction in direction_list:
        map2048 = move(direction, map2048)
        
    row_maximum = []
    for row in map2048:
        row_maximum.append(max(row))
    
    return max(row_maximum)
    
    
def move(direction, map2048):
    N = len(map2048)
    
    map_copy = []
    
    if direction == 0:
        for i in range(N): # row
            tmp = []
            for j in reversed(range(N)): # col
                val = map2048[i][j]
                if val == 0:
                    continue
                elif len(tmp) == 0: # tmp empty
                    tmp.append(val)
                elif tmp[0] == 0: # in previous time, we do sum
                    tmp[0] = val
                elif tmp[0] == val: # sum
                    tmp[0] = val*2
                    tmp.insert(0,0)
                else: # different number
                    tmp.insert(0,val)
            for j in range(len(tmp), N):
                tmp.insert(0,0) # insert(index, value)
            
            map_copy.append(tmp)
    
    elif direction == 1:
        for i in range(N): # row
            tmp = []
            cur = 0
            for j in range(N): # col
                val = map2048[i][j]
                if val == 0:
                    continue
                elif len(tmp) == 0:  # tmp empty
                    tmp.append(val)
                elif tmp[cur] == 0: # in previous time, we do sum
                    tmp[cur] = val
                elif tmp[cur] == val:
                    tmp[cur] = val*2
                    tmp.append(0)
                    cur += 1
                else:
                    tmp.append(val)
                    cur += 1
            for j in range(len(tmp), N):
                tmp.append(0) # insert(index, value)
            
            map_copy.append(tmp)
            
    elif direction == 2:
        for i in range(N): # col
            tmp = []
            cur = 0
            for j in range(N): # row
                val = map2048[j][i]
                if val == 0:
                    continue
                elif len(tmp) == 0:
                    tmp.append(val)
                elif tmp[cur] == 0:
                    tmp[cur] = val
                elif tmp[cur] == val:
                    tmp[cur] = val*2
                    tmp.append(0)
                    cur += 1
                else:
                    tmp.append(val)
                    cur += 1
            for j in range(len(tmp), N):
                tmp.append(0) # insert(index, value)
            
            if len(map_copy) == 0:
                for i in range(N):
                    map_copy.append([tmp[i]])
            else:
                for i in range(N):
                    map_copy[i].append(tmp[i])
                    
    else:
        for i in range(N): # col
            tmp = []
            for j in reversed(range(N)): # row
                val = map2048[j][i]
                if val == 0:
                    continue
                elif len(tmp) == 0: # tmp empty 
                    tmp.append(val)
                elif tmp[0] == 0: # in previous time, we do sum
                    tmp[0] = val
                elif tmp[0] == val:
                    tmp[0] = val*2
                    tmp.insert(0,0)
                else:
                    tmp.insert(0,val)
            for j in range(len(tmp), N):
                tmp.insert(0,0) # insert(index, value)
            
            if len(map_copy) == 0:
                for i in range(N):
                    map_copy.append([tmp[i]])
            else:
                for i in range(N):
                    map_copy[i].append(tmp[i])
    
    return map_copy


def show(map2048):
    for row in map2048:
        print(row)


if __name__ == '__main__':
    main()