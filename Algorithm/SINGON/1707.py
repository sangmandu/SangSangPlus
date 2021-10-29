import sys
from collections import deque
input = sys.stdin.readline
def bfs(i):
    visited[i] = 1
    q = deque()
    q.append(i)
    while q:
        a = q.popleft()
        for i in s[a]:
            if visited[i] ==0:
                visited[i] = -visited[a]
                q.append(i)
            elif visited[i] == visited[a]:
                return False
    return True
if __name__ == "__main__":
    K = int(input()) #Test case
    for _ in range(K):
        V, E = map(int, input().split())
        Possible = True #가능한지 불가능한지 이진 분류
        s = [[] for _ in range(V+1)] #연결 되어있는 것을 연결시키기 위함
        visited = [0]*(V+1) #1, -1로 이분법하기 위함
        for _ in range(E):
            a, b = map(int, input().split())
            s[a].append(b)
            s[b].append(a)
        for j in range(1, V+1):
            if visited[j] == 0:
                Possible = bfs(j)
                if not Possible:
                    break
        print("YES" if Possible else "NO")