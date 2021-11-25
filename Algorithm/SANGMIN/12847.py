'''
https://www.acmicpc.net/problem/12847
꿀 아르바이트
[풀이]
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
T = list(map(int, input().split()))

ans = pay = sum(T[:m])
for ed in range(m, len(T)):
    pay += T[ed] - T[ed-m]
    ans = max(ans, pay)
print(ans)
