'''
https://www.acmicpc.net/problem/1149
RGB거리
[풀이]
1. 각각의 경우는 3가지 색을 고르는 경우가 존재한다.
2. 현재는 이전에서 2가지 색을 고르는 경우에서만 이어질 수 있다.
3. 현재의 비용은 이전에서 2가지 색을 고르는 경우 중 최소에서 이어지는 것을 택해야 한다.
'''
import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [cost[0]] + [[0]*3 for _ in range(n-1)]
for y in range(1, n):
    for x in range(3):
        a, b = (x+1) % 3, (x+2) % 3
        dp[y][x] = min(dp[y-1][a], dp[y-1][b]) + cost[y][x]
print(min(dp[n-1]))
