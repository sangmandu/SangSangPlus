import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) #파이썬 기본 재귀 깊이 제한은 1000이므로 매우 얕음. 따라서 재귀를 사용할 것이라면 위와 같은 코드를 상단에 쓰는 것은 필수이다.
def dfs(x, y):
    global cnt
    graph[x][y] = 0
    cnt +=1
    for i in range(4):
        Nx = x +dx[i]
        My = y + dy[i]
        if Nx < 0 or Nx>N-1 or My<0 or My>M-1:
            continue
        if graph[Nx][My] ==1:
            dfs(Nx, My)
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        M, N, K = map(int,input().split())
        graph = [[0]*M for _ in range(N)]
        visited = []
        for _ in range(K):
            a, b = map(int, input().split())
            graph[b][a] = 1
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 1:
                    cnt = 0
                    dfs(i, j)
                    visited.append(cnt)
        print(len(visited))
