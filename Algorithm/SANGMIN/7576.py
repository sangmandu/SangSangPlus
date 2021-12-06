'''
https://www.acmicpc.net/problem/7576
토마토
[풀이]
'''
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
stack, save = [], []
for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            stack.append((y, x))

while stack or save:
    if not stack:
        stack, save = save, stack
        ans += 1
    y, x = stack.pop()
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 0:
            board[ny][nx] = 1
            save.append((ny, nx))
print(-1 if sum([b.count(0) for b in board]) else ans)
