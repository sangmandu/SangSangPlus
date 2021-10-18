import sys
input = sys.stdin.readline
n = int(input())
A = [0]+list(map(int, input().split()))
dp = [0]*(n+1)
for i in range(1,n+1):
    dp[i] = max(A[i], dp[i-1]+A[i])
print(max(dp[1:]))
