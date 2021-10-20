import sys
from collections import deque
input = sys.stdin.readline
def DFS(N, V, visit_dfs):
    visit_dfs[V] = 1
    print(V, end = " ")
    for i in range(1, N+1):
        if visit_dfs[i] == 0 and graph[V][i] == 1:
            DFS(N,i, visit_dfs)
def BFS(N, V, visit_bfs):
    q = deque()
    q.append(V)
    visit_bfs[V] = 1
    while q:
        V = q.popleft()
        print(V, end = " ")
        for i in range(1, N+1):
            if visit_bfs[i] == 0 and graph[V][i] == 1:
                q.append(i)
                visit_bfs[i] =1
if __name__ == "__main__":
    N, M, V = map(int, input().split())
    graph = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b] = graph[b][a] = 1
    visit_dfs = [0]*(N+1)
    visit_bfs = [0]*(N+1)
    DFS(N, V, visit_dfs)
    print()
    BFS(N, V, visit_bfs)
