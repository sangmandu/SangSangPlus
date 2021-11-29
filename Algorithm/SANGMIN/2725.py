'''
https://www.acmicpc.net/problem/2725
어두운 건 무서워
[풀이]
'''
import sys
input = sys.stdin.readline

import math
dp = [0] * 1001
dp[1] = 3
for y in range(2, 1001):
    cnt = 0
    for x in range(1, y):
        cnt += 2 if math.gcd(y, x) == 1 else 0
    dp[y] = dp[y-1] + cnt

for _ in range(int(input())):
    n = int(input())
    print(dp[n])
