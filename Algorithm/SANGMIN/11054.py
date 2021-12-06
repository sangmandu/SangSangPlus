'''
https://www.acmicpc.net/problem/11054
가장 긴 바이토닉 부분 수열
[풀이]
1. 양쪽으로 LIS를 적용한다.
=> Key point : 내가 어떤애보다 크다면 적어도 그녀석이 가지고 있는 dp값보다 1은 크겠지!
2. 왼쪽 DP와 오른쪽 DP를 종합해서 최댓값을 반환한다. 대신, 자기자신이 두번 더해지므로 -1
'''
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
ldp, rdp = [1]*n, [1]*n

for i in range(1, n):
    for j in range(i):
        if lst[j] < lst[i]:
            ldp[i] = max(ldp[j]+1, ldp[i])
        if lst[n-1-j] < lst[n-1-i]:
            rdp[n-1-i] = max(rdp[n-1-j]+1, rdp[n-1-i])
print(max([l+r-1 for l, r in zip(ldp, rdp)]))
