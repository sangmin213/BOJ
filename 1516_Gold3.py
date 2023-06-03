def main():
    N = int(input())
    build = [list(map(int, input().split()))[:-1] for _ in range(N)]
    build.insert(0, None)
    dp = [0] * (N+1)
    visited = [0] * (N+1) # 0: 방문X, 1: 방문 & 선 건물 필요, 2: 방문 완료

    for i in range(1,N+1):
        if visited[i] == 2:
            continue
        prev_build = build[i][1:]
        # 선축건물 소요 시간부터 측정
        while len(prev_build) != 0:
            this = prev_build.pop(0)
            if visited[this] == 2:
                continue
            elif len(build[this][1:]) == 0: # 선축건물 없는 건물
                dp[this] = build[this][0]
                visited[this] = 2
            elif visited[this] == 1:
                for prev in build[this][1:]:
                    dp[this] = max(dp[this], dp[prev])
                dp[this] += build[this][0]
                visited[this] = 2
            else:
                prev_build = build[this][1:] + [this] + prev_build
                visited[this] = 1
        for prev in build[i][1:]:
            dp[i] = max(dp[i], dp[prev])
        dp[i] += build[i][0]
        visited[i] = 2

    for result in dp[1:]:
        print(result)

    return

if __name__ == '__main__':
    main()