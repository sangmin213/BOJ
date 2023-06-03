'''
    미완
'''

def str2list(string):
    mylist = []
    mylist[:0] = string # reference를 넘김으로써 string을 list 형식으로 출력해줌.
    mylist = list(map(int, mylist))
    return mylist

def greedy(before, after):
    cnt = 0
    length = len(before)
    while before != after:
        best_change = 0
        best_idx = 0
        for i, val in enumerate(before):
            tmp = 0
            if i==0:
                if val != after[i]: tmp += 1
                if before[i+1] != after[i+1]: tmp+=1
            elif i==length-1:
                if val != after[i]: tmp += 1
                if before[i-1] != after[i-1]: tmp += 1
            else:
                if before[i-1] != after[i-1]: tmp += 1
                if val != after[i]: tmp += 1
                if before[i+1] != after[i+1]: tmp += 1
            
            if tmp > best_change:
                best_change = tmp
                best_idx = i

            if tmp == 3:
                break
        
        # change
        if best_idx == 0:
            before[best_idx] = (before[best_idx] + 1) % 2 # 0 -> 1, 1 -> 0 (=2 % 2)
            before[best_idx+1] = (before[best_idx+1] + 1) % 2 
        elif best_idx == length-1:
            before[best_idx] = (before[best_idx] + 1) % 2
            before[best_idx-1] = (before[best_idx-1] + 1) % 2 
        else:
            before[best_idx-1] = (before[best_idx-1] + 1) % 2 
            before[best_idx] = (before[best_idx] + 1) % 2 
            before[best_idx+1] = (before[best_idx+1] + 1) % 2 

        cnt += 1
    
    return cnt


def main():
    N = int(input())
    before = str2list(input())
    after = str2list(input())
    print(greedy(before, after))
    
    return

if __name__ == '__main__':
    main()