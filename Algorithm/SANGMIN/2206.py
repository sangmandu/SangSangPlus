'''
https://www.acmicpc.net/problem/2206
벽 부수고 이동하기
[풀이]
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

from collections import deque
stack = deque([(0, 0, 1, 1)])
while stack:
    y, x, dist, flag = stack.popleft()
    if y == N-1 and x == M-1:
        print(dist)
        break
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M:
            if board[ny][nx] == '1':
                if flag:
                    stack.append((ny, nx, dist+1, 0))
            elif board[ny][nx] == '0':
                board[ny][nx] = [N*M, dist+1] if flag else [dist+1, N*M]
                stack.append((ny, nx, dist + 1, flag))
            elif board[ny][nx][flag] > dist+1:
                board[ny][nx][flag] = dist+1
                stack.append((ny, nx, dist+1, flag))

else:
    print(-1)
