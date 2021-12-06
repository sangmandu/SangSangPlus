'''
https://www.acmicpc.net/problem/2798
블랙잭
[풀이]
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
max_total = 0
try:
    for x in range(n-2):
        for y in range(x+1, n-1):
            for z in range(y+1, n):
                total = cards[x] + cards[y] + cards[z]
                if total < m:
                    max_total = max(max_total, total)
                    continue
                if total == m:
                    raise ValueError
    print(max_total)
except:
    print(m)
