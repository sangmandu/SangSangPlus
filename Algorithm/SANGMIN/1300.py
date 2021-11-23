'''
https://www.acmicpc.net/problem/1300
K번째 수
[풀이]
'''
import sys
input = sys.stdin.readline

N, k = int(input()), int(input())
left, right = 1, k
while left <= right:
    mid = (left + right) // 2
    total = sum([min(mid // i, N) for i in range(1, N+1)])
    if total >= k:
        right = mid - 1
        ans = mid
    else:
        left = mid + 1
print(ans)
