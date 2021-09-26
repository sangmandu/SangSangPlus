'''
https://www.acmicpc.net/problem/2775
부녀회장이 될테야
[풀이]
'''
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k, n = map(int, [input(), input()])
    apart = [[1] + [0] * (n-1) for _ in range(k+1)]

    for x in range(1, n):
        apart[0][x] = x+1
    for y in range(1, k+1):
        for x in range(1, n):
            apart[y][x] = apart[y-1][x] + apart[y][x-1]

    print(apart[k][n-1])
