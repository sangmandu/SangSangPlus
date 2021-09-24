import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input())
max_h, min_h = [-int(input())], []
print(-max_h[0])

for i in range(2, n + 1):
    m = int(input())
    if len(min_h) == len(max_h):
        heappush(max_h, -m)
    else:
        heappush(min_h, m)

    if -max_h[0] > min_h[0]:
        a, b = heappop(max_h), heappop(min_h)
        heappush(max_h, -b)
        heappush(min_h, -a)
    print(-max_h[0])
