'''
https://www.acmicpc.net/problem/1012
유기농 배추
[풀이]
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    answer = 0
    for _ in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1
    for y in range(N):
        for x in range(M):
            cnt = 0
            if board[y][x] == 1:
                cnt += 1
                board[y][x] = 2
                stack = [(y, x)]
                while stack:
                    sy, sx = stack.pop()
                    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        ny, nx = sy+dy, sx+dx
                        if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 1:
                            board[ny][nx] = 2
                            stack.append((ny, nx))
                            cnt += 1
            if cnt:
                answer += 1
    print(answer)
