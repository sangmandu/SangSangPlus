'''
https://www.acmicpc.net/problem/2667
단지번호붙이기
[풀이]
'''
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, list(input().strip()))) for _ in range(n)]
answer = []
for y in range(n):
    for x in range(n):
        cnt = 0
        if board[y][x] == 1:
            cnt += 1
            board[y][x] = 2
            stack = [(y, x)]
            while stack:
                sy, sx = stack.pop()
                for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ny, nx = sy+dy, sx+dx
                    if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 1:
                        board[ny][nx] = 2
                        stack.append((ny, nx))
                        cnt += 1
        if cnt:
            answer.append(cnt)
print(len(answer), *sorted(answer), sep='\n')
