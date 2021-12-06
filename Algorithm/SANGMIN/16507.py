'''
https://www.acmicpc.net/problem/16507
어두운 건 무서워
[풀이]
'''
import sys
input = sys.stdin.readline

from itertools import accumulate
R, C, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
lst = [list(map(int, input().split())) for _ in range(Q)]

dp = [[0] * (C+1) for _ in range(R+1)]
for y in range(1, R+1):
    for x in range(1, C+1):
        dp[y][x] = dp[y-1][x] + dp[y][x-1] + board[y-1][x-1] - dp[y-1][x-1]

for r1, c1, r2, c2 in lst:
    _sum = dp[r2][c2] - dp[r1-1][c2] - dp[r2][c1-1] + dp[r1-1][c1-1]
    print(_sum // ((r2-r1+1)*(c2-c1+1)))
