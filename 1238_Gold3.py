from copy import deepcopy
import heapq

def main():
    N, M, X = tuple(map(int, input().split()))
    INF = 1e9

    graph = [[] for _ in range(N+1)]

    visited = [False] * (N+1)
    distance = [INF] * (N+1)

    for n in range(M):
        S, E, W = tuple(map(int, input().split()))
        graph[S].append((E, W))             # 도착 지점 & 거리 가중치

    result = [dijkstra(i, graph, deepcopy(distance)) for i in range(N+1)]
    final_result = [result[i][X]+result[X][i] for i in range(1,N+1)]
    
    print(max(final_result))


def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start)) # 우선순위, 값 형태로 들어감.
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 우선순위가 가장 낮은 값(가장 적은 거리)

        if distance[now] < dist: # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드
            continue

        for i in graph[now]:
            if dist+i[1] < distance[i[0]]: # 기존에 입력되어있는 값보다 크다면
                distance[i[0]] = dist+i[1]
                heapq.heappush(q, (dist+i[1], i[0]))

    return distance


if __name__ == '__main__':
    main()