import sys
input = sys.stdin.readline
N = int(input())
X = list(tuple(map(int,input().split())) for _ in range(N))
X.sort()
dp = [0]*101
for i in range(0, N):
    maximum = 0
    for j in range(i):
        if X[j][1] < X[i][1]:
            if dp[j] >= maximum:
                maximum = dp[j]

    dp[i] = maximum+1
Y = max(dp)
print(N-Y)    
