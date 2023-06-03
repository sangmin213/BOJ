'''
DP
마지막에서부터 뒤로 돌아감
Nth에 최대치 계산
N-1th에 최대치 계산
N-2th에 최대치 계산
...
'''

import sys

def main():
    N = int(sys.stdin.readline())
    T, P = [], []
    for i in range(N):
        t, p = tuple(map(int, sys.stdin.readline().split()))
        T.append(t)
        P.append(p)
    dp = [0 for _ in range(N)]
    for i in reversed(range(N)):
        DP(N, i, T, P, dp)
    
    # result
    print(dp[0])
        
            
def DP(N, i, T, P, dp):
    # 오늘 받은 업무가 기한 안에 끝날 경우
    if i+T[i] <= N:
        if i+T[i] < N: # 오늘 받은 업무가 끝나고 다음 일을 모색해볼 수 있는 경우
            try: # 오늘 받은 업무 소요 기간이 하루(T[i]=1)가 아닌 경우 
                if P[i]+dp[i+T[i]] > max(dp[i+1 : i+T[i]]): # 오늘 받은 업무를 수행했을 경우의 예상 급여가 더 큰 경우
                    dp[i] = P[i]+dp[i+T[i]]
                else: # 오늘 받은 업무를 수행 안 했을 경우의 예상 급여가 더 큰 경우
                    dp[i] = max(dp[i+1 : i+T[i]])
            except: # 오늘 받은 업무 소요 기간이 하루(T[i]=1)인 경우 
                dp[i] = P[i] + dp[i+1]
        else: # 오늘 받은 업무가 끝나고 다음 일을 모색해볼 수 없는 경우
            try: 
                if P[i] > max(dp[i+1:]): # 오늘 받은 업무를 수행했을 경우의 예상 급여가 더 큰 경우
                    dp[i] = P[i]
                else:
                    dp[i] = max(dp[i+1:])
            except: # i = N-1 인 경우 == i+1=N 이어서 dp의 index를 넘어가는 경우
                dp[i] = P[i]
                
    else:
        try:
            dp[i] = max(dp[i+1:]) # i+1이 N보다 작은 경우
        except:
            dp[i] = 0 # i+1이 N인 경우

            
if __name__ == '__main__':
    main()