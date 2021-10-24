import sys
from collections import deque
input = sys.stdin.readline
def bfs(q):
    while q:
        a, b, c = q.popleft()
        graph[c][b][a] =1
        for i in range(6):
            x = a + dx[i]
            y = b + dy[i]
            z = c + dz[i]
            if 0<=x<M and 0<=y<N and 0<=z<K and box[z][y][x] == 0 and graph[z][y][x] ==0:
                q.append([x, y, z])
                box[z][y][x] = box[c][b][a] +1
                graph[z][y][x] = 1
                
if __name__=="__main__":
    M, N, K = map(int, input().split())
    box = [list(list(map(int, input().split()))for _ in range(N)) for _ in range(K)]
    graph = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(K)]
    cnt = 0
    possible = True
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    q = deque()
    for z in range(K):
        for y in range(N):
            for x in range(M):
                if box[z][y][x] == 1:
                    q.append([x,y,z])
    bfs(q)
    for z in range(K):
        for y in range(N):
            for x in range(M):
                if box[z][y][x] == 0:
                    possible = False
                cnt = max(cnt, box[z][y][x])
    if possible == False:
        print(-1)
    else:
        print(cnt-1)
