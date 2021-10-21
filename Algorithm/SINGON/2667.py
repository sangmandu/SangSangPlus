import sys
input = sys.stdin.readline
def dfs(x, y): #dfs 함수 정의
    global cnt
    graph[x][y] = 0
    cnt += 1
    for i in range(4):
        Nx = x + dx[i]
        Ny = y + dy[i]
        if Nx < 1 or Nx>N or Ny<1 or Ny>N: #주어진 범위를 벗어나면 안됨.
            continue
        if graph[Nx][Ny] == 1:
            dfs(Nx,Ny)
    
if __name__ == "__main__":
    N = int(input())
    graph = [[0]*(N+1) for _ in range(N+1)]
    visited = []
    for i in range(1,N+1):
        A = '0'+str(input().strip())
        for j in range(1,N+1):
            graph[i][j] = int(A[j])
    cnt = 0    
    dx = [1, -1, 0 ,0] #방향 설정
    dy = [0, 0, 1, -1]
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][j] ==1:
                cnt = 0
                dfs(i, j)
                visited.append(cnt)
print(len(visited))
visited.sort()
for i in visited:
    print(i)
