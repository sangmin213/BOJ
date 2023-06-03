''' 목표
K에 가장 근접한 무게 W & 가장 높은 V
1. W의 조합 모두 구하기
2. 그 중 V가 가장 높은 거 찾기
--
W = 1 중에 가장 V 높은 것 만들기
W = 2 중에 가장 V 높은 것 만들기
W = 3 중에 가장 V 높은 것 만들기
W = 4 중에 가장 V 높은 것 만들기
...
재귀함수

'''

import sys

# N, K = tuple(map(int, sys.stdin.readline().split()))
f = open("./input.txt")
N, K = tuple(map(int, f.readline().split()))

mylist = {}
for _ in range(N):
    W, V = tuple(map(int, f.readline().split()))
    if W in mylist.keys():
        mylist[W].append(V)
    else:
        mylist[W]=[V]

keys = sorted(list(mylist.keys())) # W(key) 크기 순서대로 정리
for key in keys:
    mylist[key].sort(reverse=True) # 각 W 별 V 높은 순서대로 정리
    
# 각 key를 몇 번 방문했는지 파악해서 해당 weight 중 몇 번째 value를 꺼내야 하는지 확인(같은 weight이 여러 개 있을 경우)
visited = {}
for key in keys:
    visited[key] = 0

# 재귀
dp_result = [-1 for _ in range(K+1)]
def DP(weight):
    visit = visited.copy()
    # 이미 해당 weight를 위한 최대 Value 계산이 끝나있다면 그대로 반환
    if dp_result[weight] != -1:
        return dp_result[weight]
    
    # 아니라면 계산 시작
    for w in range(1, weight//2+1):
        if w in keys:
            idx = visit[key]
            visit[key] = idx+1 # visit 갱신
            tmp = mylist[w][idx] # 이번 idx의 value 가져옴
        else:
            DP(w)
    
    
    return



