'''
https://www.acmicpc.net/problem/15093
카드 합체 놀이
[풀이]
1. 매번 작은 수를 골라서 더해야 가장 작은 값을 얻을 수 있다.
2. 따라서, 매번 오름차순으로 정렬되는 최소힙을 사용한다.
'''
import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline

n, m = map(int, input().split())
h = list(map(int, input().split()))
heapify(h)
for _ in range(m):
    a, b = heappop(h), heappop(h)
    heappush(h, a+b)
    heappush(h, a+b)
print(sum(h))
