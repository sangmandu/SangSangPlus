'''
https://www.acmicpc.net/problem/2110
공유기 설치
[풀이]
'''
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
lst = sorted([int(input()) for _ in range(N)])

left, right = 0, max(lst)
while left <= right:
    mid = (left + right) // 2
    cnt, pre = C-1, lst[0]
    for item in lst[1:]:
        if item - pre >= mid:
            pre = item
            cnt -= 1
            if not cnt:
                break
    if cnt:
        right = mid - 1
    else:
        left, ans = mid + 1, mid

print(ans)
