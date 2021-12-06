'''
https://www.acmicpc.net/problem/1260
DFS와 BFS
[풀이]
'''
import sys
input = sys.stdin.readline

from collections import defaultdict, deque
n, m, v = map(int, input().split())
board = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

stack, visited = [v], []
while stack:
    item = stack.pop()
    if item not in visited:
        visited.append(item)
        stack += sorted([node for node in board[item] if node not in visited])[::-1]
print(*visited)

stack, visited = deque([v]), []
while stack:
    item = stack.popleft()
    if item not in visited:
        visited.append(item)
        stack += sorted([node for node in board[item] if node not in visited])
print(*visited)
