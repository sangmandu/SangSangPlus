import sys
from collections import deque
input = sys.stdin.readline
def bfs(n, k):
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x ==k:
            print(graph[x])
            break
        for nx in [x-1, x+1, 2*x]: #선택의 가지수 3가지
            if 0<=nx<200000 and graph[nx] == 0: #이동하기 위한 필수 조건
                graph[nx] = graph[x] + 1 #이동한 곳은 시간이 +1
                q.append(nx)

if __name__== "__main__":
    N, K = map(int, input().split())
    graph = [0]*(200000) # graph[x]의 value는 최소이동시간.
    bfs(N, K)

    

