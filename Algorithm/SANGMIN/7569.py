'''
https://www.acmicpc.net/problem/7569
토마토
[풀이]
'''
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
ans = 0
stack, save = [], []
for z in range(H):
    for y in range(N):
        for x in range(M):
            if board[z][y][x] == 1:
                stack.append((z, y, x))

while stack or save:
    if not stack:
        stack, save = save, stack
        ans += 1
    z, y, x = stack.pop()
    for dz, dy, dx in [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]:
        nz, ny, nx = z + dz, y + dy, x + dx
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and board[nz][ny][nx] == 0:
            board[nz][ny][nx] = 1
            save.append((nz, ny, nx))
print(-1 if sum([b.count(0) for by in board for b in by]) else ans)
