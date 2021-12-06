'''
https://www.acmicpc.net/problem/1018
체스판 다시 칠하기
[풀이]
'''
import sys
input = sys.stdin.readline

a, b = "WB"*4, "BW"*4
chess = [[a, b] * 4, [b, a] * 4]

n, m = map(int, input().split())
board = [input() for _ in range(n)]
min_cnt = 64
for c in chess:
    for sy in range(n-7):
        for sx in range(m-7):
            min_cnt = min(min_cnt, [1 if board[sy+y][sx+x] == c[y][x] else 0 for y in range(8) for x in range(8)].count(0))
print(min_cnt)






