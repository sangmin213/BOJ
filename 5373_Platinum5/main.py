'''
윗 면은 흰색, 아랫 면은 노란색, 앞 면은 빨간색, 뒷 면은 오렌지색, 왼쪽 면은 초록색, 오른쪽 면은 파란색
'''

from copy import deepcopy

right_rotate = lambda x : [list(xx) for xx in list(zip(*x[::-1]))]
left_rotate = lambda x : [list(xx) for xx in reversed(list(zip(*x)))]

def main():
    N = int(input())

    rotations = []
    for i in range(N):
        input()
        rotations.append(list(input().split()))

    # cube: U, D, F, B, L, R    
    cube = [[['w' for i in range(3)] for j in range(3)],
           [['y' for i in range(3)] for j in range(3)],
           [['r' for i in range(3)] for j in range(3)],
           [['o' for i in range(3)] for j in range(3)],
           [['g' for i in range(3)] for j in range(3)],
           [['b' for i in range(3)] for j in range(3)]]
    
    # print(rotations)
    
    for rotation in rotations:
        rotate(deepcopy(cube), rotation)

def rotate(cube, rotation):
    for r in rotation:
        if r=='U+': # f->l->b->r->f
            cube[0] = right_rotate(cube[0])
            tmp = deepcopy(cube[4][0]) # l
            cube[4][0] = cube[2][0] # f->l
            cube[2][0] = cube[5][0] # r->f
            cube[5][0] = cube[3][0] # b->r
            cube[3][0] = tmp # l->b
        elif r=='U-': # f<-l<-b<-r<-f
            cube[0] = left_rotate(cube[0])
            tmp = deepcopy(cube[2][0]) # f
            cube[2][0] = cube[4][0] # l->f
            cube[4][0] = cube[3][0] # b->l
            cube[3][0] = cube[5][0] # r->b
            cube[5][0] = tmp # f->r
        elif r=='D+': # f<-l<-b<-r<-f # U+와 반대 == U-와 동일
            cube[1] = right_rotate(cube[1])
            tmp = deepcopy(cube[2][-1]) # f
            cube[2][-1] = cube[4][-1] # l->f
            cube[4][-1] = cube[3][-1] # f->r
            cube[3][-1] = cube[5][-1] # r->b
            cube[5][-1] = tmp # f->r
        elif r=='D-': # f->l->b->r->f
            cube[1] = left_rotate(cube[1])
            tmp = deepcopy(cube[4][-1])
            cube[4][-1] = cube[2][-1] # f->l
            cube[2][-1] = cube[5][-1] # r->f
            cube[5][-1] = cube[3][-1] # b->r
            cube[3][-1] = tmp # l->b
        elif r=='F+':
            cube[2] = right_rotate(cube[2])
            tmp = deepcopy(cube[0][-1]) # u
            cube[0][-1] = list(reversed(list(list(zip(*cube[4]))[-1]))) # l -> u
            cube[4][0][-1], cube[4][1][-1], cube[4][2][-1] = tuple(cube[1][0])# d -> l
            cube[1][0] = list(reversed(list(list(zip(*cube[5]))[0]))) # r -> d
            cube[5][0][0], cube[5][1][0], cube[5][2][0] = tuple(tmp) # u -> r
        elif r=='F-':
            cube[2] = left_rotate(cube[2])
            tmp = deepcopy(list(reversed(cube[1][0]))) # d
            cube[1][0] = list(list(zip(*cube[4]))[-1]) # l -> d
            cube[4][0][-1], cube[4][1][-1], cube[4][2][-1] = tuple(list(reversed(cube[0][-1])))# u -> l
            cube[0][-1] = list(list(zip(*cube[5]))[0]) # r -> u
            cube[5][0][0], cube[5][1][0], cube[5][2][0] = tuple(tmp) # d -> r
        elif r=='B+':
            cube[3] = right_rotate(cube[3])
            tmp = deepcopy(list(reversed(cube[1][-1]))) # d
            cube[1][-1] = list(list(zip(*cube[4]))[0]) # l -> d
            cube[4][0][0], cube[4][1][0], cube[4][2][0] = tuple(list(reversed(cube[0][0])))# u -> l
            cube[0][0] = list(list(zip(*cube[5]))[-1]) # r -> u
            cube[5][0][-1], cube[5][1][-1], cube[5][2][-1] = tuple(tmp) # d -> r
        elif r=='B-':
            cube[3] = left_rotate(cube[3])
            tmp = deepcopy(cube[0][0]) # u
            cube[0][0] = list(reversed(list(list(zip(*cube[4]))[0]))) # l -> u
            cube[4][0][0], cube[4][1][0], cube[4][2][0] = tuple(cube[1][-1])# d -> l
            cube[1][-1] = list(reversed(list(list(zip(*cube[5]))[-1]))) # r -> d
            cube[5][0][-1], cube[5][1][-1], cube[5][2][-1] = tuple(tmp) # u -> r
        elif r=='L+':
            cube[4] = right_rotate(cube[4])
            tmp = deepcopy(list(zip(*cube[2]))[0]) # f
            cube[2][0][0], cube[2][1][0], cube[2][2][0] = list(zip(*cube[0]))[0] # u -> f
            cube[0][2][0], cube[0][1][0], cube[0][0][0] = list(zip(*cube[3]))[-1] # b -> u
            cube[3][2][-1], cube[3][1][-1], cube[3][0][-1] = list(zip(*cube[1]))[0] # d -> b
            cube[1][0][0], cube[1][1][0], cube[1][2][0] = tmp # f -> d
        elif r=='L-':
            cube[4] = left_rotate(cube[4])
            tmp = deepcopy(list(zip(*cube[2]))[0]) # f
            cube[2][0][0], cube[2][1][0], cube[2][2][0] = list(zip(*cube[1]))[0] # d -> f
            cube[1][2][0], cube[1][1][0], cube[1][0][0] = list(zip(*cube[3]))[-1] # b -> d
            cube[3][2][-1], cube[3][1][-1], cube[3][0][-1] = list(zip(*cube[0]))[0] # u -> b
            cube[0][0][0], cube[0][1][0], cube[0][2][0] = tmp # f -> u
        elif r=='R+':
            cube[5] = right_rotate(cube[5])
            tmp = list(zip(*cube[2]))[-1] # f
            cube[2][0][-1], cube[2][1][-1], cube[2][2][-1] = list(zip(*cube[1]))[-1] # d -> f
            cube[1][2][-1], cube[1][1][-1], cube[1][0][-1] = list(zip(*cube[3]))[0] # b -> d
            cube[3][2][0], cube[3][1][0], cube[3][0][0] = list(zip(*cube[0]))[-1] # u -> b
            cube[0][0][-1], cube[0][1][-1], cube[0][2][-1] = tmp # f -> u
        elif r=='R-':
            cube[5] = left_rotate(cube[5])
            tmp = list(zip(*cube[2]))[-1] # f
            cube[2][0][-1], cube[2][1][-1], cube[2][2][-1] = list(zip(*cube[0]))[-1] # u -> f
            cube[0][2][-1], cube[0][1][-1], cube[0][0][-1] = list(zip(*cube[3]))[0] # b -> u
            cube[3][2][0], cube[3][1][0], cube[3][0][0] = list(zip(*cube[1]))[-1] # d -> b
            cube[1][0][-1], cube[1][1][-1], cube[1][2][-1] = tmp # f -> d
            
    for row in cube[0]:
        for r in row:
            print(r,end="")
        print()
    
    return cube
            
if __name__ == '__main__':
    main()