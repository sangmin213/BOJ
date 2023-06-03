def r_op(matrix):
    new_matrix = []
    for row in matrix:
        item2cnt, cnt2item = {}, {}
        for ele in row:
            if ele == 0:
                continue
            if ele in item2cnt.keys(): item2cnt[ele] += 1
            else:   item2cnt[ele] = 1 # item 개수 저장

            if item2cnt[ele] in cnt2item.keys(): cnt2item[item2cnt[ele]].append(ele)
            else:   cnt2item[item2cnt[ele]] = [ele] # 각 개수별 item 저장

            if item2cnt[ele] > 1:
                cnt2item[item2cnt[ele] - 1].remove(ele) # 이전 개수에 있던 item 삭제
        new_row = []
        for cnt in sorted(cnt2item):
            tmp = sorted(cnt2item[cnt])
            for ele in tmp:
                new_row += [ele, cnt]
        new_matrix.append(new_row)
    
    max_len = 0
    for row in new_matrix:
        if len(row) > max_len:  max_len = len(row)
    
    for row in new_matrix:
        row += [0 for i in range(max_len - len(row))]

    return new_matrix

rotation = lambda x : [list(xx) for xx in list(zip(*x))]

def c_op(matrix):
    matrix = rotation(matrix)
    matrix = r_op(matrix)
    matrix = rotation(matrix)

    return matrix


def main():
    r, c, k = map(int,input().split())
    matrix = [list(map(int,input().split())) for i in range(3)]
    result = -1
    t = 0
    while t <= 100:
        if len(matrix) >= r and len(matrix[0]) >= c and matrix[r-1][c-1] == k:
            result = t
            break
        
        if len(matrix) >= len(matrix[0]):   matrix = r_op(matrix)
        else:   matrix = c_op(matrix)

        t += 1

    print(result)
    return

if __name__ == '__main__':
    main()