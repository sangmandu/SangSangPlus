'''
https://www.acmicpc.net/problem/1978
소수 찾기
[풀이]
'''
import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))

sieve = [False] * 2 + [True] * (max(m)-1)
for i in range(2, int(max(m) ** 0.5)+1):
    if sieve[i]:
        for j in range(i+i, max(m)+1, i):
            sieve[j] = False
print(len([i for i in m if sieve[i]]))
