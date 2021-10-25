from collections import deque
import sys
input = sys.stdin.readline
def bfs(q):
    while q:
        a, b = q.popleft()
        visited[b][a] = 1
        for i in range(4):
            mx = a + dx[i]
            ny = b + dy[i]
            if 0<= mx <m and 0<= ny< n and box[ny][mx]==0 and visited[ny][mx] ==0:
                q.append([mx, ny])
                box[ny][mx] = box[b][a] +1
                visited[ny][mx] = 1

if __name__=="__main__":
    m, n = map(int, input().split())
    box = list(list(map(int, input().split())) for _ in range(n))
    visited = [[0 for _ in range(m)]for _ in range(n)]
    cnt = 0
    possible = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    for y in range(n):
        for x in range(m):
            if box[y][x] == 1:
                q.append([x,y])
    bfs(q)
    for y in range(n):
        for x in range(m):
            if box[y][x] == 0:
                possible = False
            cnt = max(cnt, box[y][x])
    if possible:
        print(cnt-1)
    else:
        print(-1)