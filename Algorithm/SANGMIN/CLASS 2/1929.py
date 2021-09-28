'''
https://www.acmicpc.net/problem/1929
소수 구하기
[풀이]
'''
import sys
input = sys.stdin.readline

m, n = map(int, input().split())

sieve = [False] * 2 + [True] * (n-1)
for i in range(2, int(n ** 0.5)+1):
    if sieve[i]:
        for j in range(i+i, n+1, i):
            sieve[j] = False
print(*[i for i in range(m, n+1) if sieve[i]], sep='\n')
