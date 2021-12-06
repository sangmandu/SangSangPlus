'''
https://www.acmicpc.net/problem/2839
설탕 배달
[풀이]
'''
import sys
input = sys.stdin.readline

n = int(input())
m = 0
while n >= 0 and n % 5:
    n -= 3
    m += 1
if n >= 0: print(n // 5 + m)
else: print(-1)

