import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    m = int(input())
    if m:
        heappush(h, m)
        continue
    if len(h):
        print(heappop(h))
    else:
        print(0)
