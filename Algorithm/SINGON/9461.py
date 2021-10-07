import sys
input = sys.stdin.readline
def solution(N):
    dp = [0]*101
    dp[1] = dp[2] = dp[3] = 1
    dp[4] = dp[5] = 2
    for i in range(6,101):
        dp[i] = dp[i-1] + dp[i-5]
    return dp[N]

if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solution(N))
