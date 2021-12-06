import sys
from bisect import bisect_left
n = int(input())
A = list(map(int, input().split()))
dp = []
for i in A:
    k= bisect_left(dp,i) #자신이 들어갈 위치 k
    if len(dp) <=k:
        dp.append(i)
    else:
        dp[k] = i
print(len(dp))