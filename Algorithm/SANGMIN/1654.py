'''
https://www.acmicpc.net/problem/1654
랜선 자르기
[풀이]
'''
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]

left, right = 1, max(lst)
while left <= right:
    mid = (left + right) // 2
    total = sum([item // mid for item in lst])
    if total < N:
        right = mid - 1
    else:
        left = mid + 1
    if total >= N:
        ans = mid

print(ans)
