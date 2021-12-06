'''
https://www.acmicpc.net/problem/2805
나무 자르기
[풀이]
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

from bisect import bisect_left
from itertools import accumulate
left, right = 0, max(lst)
acc = [0] + list(accumulate(lst))
while left <= right:
    mid = (left + right) // 2
    idx = bisect_left(lst, mid)
    total = acc[-1] - acc[idx] - mid * (len(lst) - idx)
    if total >= M:
        left = mid + 1
        ans = mid
    else:
        right = mid - 1
print(ans)
