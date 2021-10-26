'''
https://www.acmicpc.net/problem/2178
미로 탐색
[풀이]
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(N)]
stack, save = [(0, 0)], []
cnt = 1
while stack or save:
    if not stack:
        stack, save = save, stack
        cnt += 1
    y, x = stack.pop()
    if (y, x) == (N-1, M-1):
        break
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 1:
            board[ny][nx] += 1
            save.append((ny, nx))
print(cnt)
