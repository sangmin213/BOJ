from sys import setrecursionlimit
setrecursionlimit(10**6) # 파이썬 최대 재귀 횟수 제한 이슈

def dp(people, village, visited, dp_list, cur):
    visited[cur] = 1

    dp_list[cur][0], dp_list[cur][1] = 0, people[cur-1]

    for neighbor in village[cur]:
        if visited[neighbor]:
            continue
        dp(people, village, visited, dp_list, neighbor)

        dp_list[cur][0] += max(dp_list[neighbor][0], dp_list[neighbor][1])
        dp_list[cur][1] += dp_list[neighbor][0]
        

def main():
    N = int(input())
    people = list(map(int,input().split()))
    village = {n:[] for n in range(N+1)}
    for _ in range(N-1):
        i, j = map(int,input().split())
        village[i].append(j)
        village[j].append(i)
    
    dp_list, visited = [[0,0] for _ in range(N+1)], [0]*(N+1)
    dp(people, village, visited, dp_list, 1)
        
    print(max(dp_list[1][0], dp_list[1][1]))

    return

if __name__ == '__main__':
    main()