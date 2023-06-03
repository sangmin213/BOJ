'''
    Python이라 DP를 반복문으로 바꿔야 통과 가능
    동일 알고리즘 C언어로 통과
'''

INF = 1e9

def DP(history, dp, novel, left, right):
    if left==right: 
        dp[left][right] = novel[left]
        return novel[left]
    if dp[left][right]!=INF:    return dp[left][right]
    for i in range(left,right):
        dp[left][right] = min(dp[left][right], DP(history, dp, novel, left, i) + DP(history, dp, novel, i+1, right))
        history[left][right] = min(history[left][right], history[left][i] + history[i+1][right] + dp[left][i] + dp[i+1][right])
    return dp[left][right]
    
def main():
    T = int(input())
    dp_list, history_list, novel_list, K_list = [], [], [], []
    for t in range(T):
        K = int(input())
        dp_list.append([[INF for i in range(K)] for j in range(K)])
        history = [[INF for i in range(K)] for j in range(K)]
        for k in range(K):
            history[k][k] = 0
        history_list.append(history)
        novel_list.append(list(map(int, input().split())))
        K_list.append(K)

    for dp, history, novel, K in zip(dp_list, history_list, novel_list, K_list):
        DP(history, dp, novel, 0, K-1)
        print(int(history[0][K-1]))
    return

if __name__ == '__main__':
    main()