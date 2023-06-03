'''
BruteForce
Backtracking(DFS)
'''

import sys

N = int(sys.stdin.readline())

score = []
for _ in range(N):
    score.append(list(map(int,sys.stdin.readline().split())))

visited = [0 for i in range(N)]
minimal = 1e10

def dfs(depth, idx, minimal):
    if depth == N//2: # 절반으로 팀 나눠진 경우
        start, link = 0,0
        for i in range(N):
            for j in range(i+1, N):
                if visited[i] and visited[j]:
                    start += score[i][j] + score[j][i]
                elif not visited[i] and not visited[j]:
                    link += score[i][j] + score[j][i]
        if minimal > abs(start - link):
            minimal = abs(start - link)
        return minimal
    
    for i in range(idx, N):
        visited[i] = 1
        minimal = dfs(depth+1, i+1, minimal)
        visited[i] = 0
    return minimal

minimal = dfs(0, 0, minimal)
print(minimal)