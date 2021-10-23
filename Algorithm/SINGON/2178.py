from collections import deque
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
# 방향성
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*M for _ in range(N)]
q = deque([(0, 0)])
visited[0][0] = 1
while q:
    x, y = q.popleft()
    if x == N-1 and y == M-1:
        print(visited[x][y])
    for i in range(4):
        Nx, My = x + dx[i], y+dy[i]
        if 0<= Nx < N and 0<= My < M:
            if visited[Nx][My] == 0 and graph[Nx][My] ==1:
                visited[Nx][My] = visited[x][y] +1
                q.append((Nx, My))
