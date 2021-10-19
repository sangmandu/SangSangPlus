'''
https://www.acmicpc.net/problem/12865
평범한 배낭
[풀이]
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0] * (k+1)
for i in range(n):
    w, v = lst[i-1]
    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], dp[j-w]+v)
print(dp[-1])
