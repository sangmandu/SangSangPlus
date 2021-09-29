import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)] # NxM 행렬 만듦
dp = [[0]*(M+1) for _ in range(N+1)] # dp = MxN 영행렬 
for i in range(1, N+1):
    for j in range(1,M+1):
        dp[i][j] = A[i-1][j-1] + dp[i][j-1]+dp[i-1][j] - dp[i-1][j-1]
# dp를 A행렬의 누적 행렬로 만든다.
K = int(input())
for _ in range(K):
    i, j, x, y = map(int,input().split())
    print(dp[x][y]-dp[x][j-1]-dp[i-1][y]+dp[i-1][j-1]) #(i,j)부터 (x,y)까지 누적 합
