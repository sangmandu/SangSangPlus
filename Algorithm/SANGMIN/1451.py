'''
https://www.acmicpc.net/problem/1451
직사각형으로 나누기
[풀이]
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [[int(i) for i in input().strip()] for _ in range(N)]

dp = [[0]*(M+1) for _ in range(N+1)]
for y in range(1, N+1):
    for x in range(1, M+1):
        dp[y][x] = dp[y-1][x] + dp[y][x-1] + board[y-1][x-1] - dp[y-1][x-1]

area = 0
for y in range(1, N+1):
    for x in range(1, M+1):
        if y == N:
            for z in range(1, N+1):
                area = max(area, dp[N][x] * (dp[z][M]-dp[z][x]) * (dp[N][M]-dp[z][M]-dp[N][x]+dp[z][x]))
            for z in range(x+1, M+1):
                area = max(area, dp[N][x] * (dp[N][z]-dp[N][x]) * (dp[N][M]-dp[N][z]))
        elif x == M:
            for z in range(1, M+1):
                area = max(area, dp[y][M] * (dp[N][z]-dp[y][z]) * (dp[N][M] - dp[N][z] - dp[y][M] + dp[y][z]))
            for z in range(y+1, N+1):
                area = max(area, dp[y][M] * (dp[z][M]-dp[y][M]) * (dp[N][M]-dp[z][M]))
        elif y == N and x == M:
            break
        else:
            area = max(area, dp[y][x] * (dp[y][M] - dp[y][x]) * (dp[N][M] - dp[y][M]))
            area = max(area, dp[y][x] * (dp[N][x] - dp[y][x]) * (dp[N][M] - dp[N][x]))
print(area)


