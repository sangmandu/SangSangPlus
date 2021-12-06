'''
https://www.acmicpc.net/problem/12015
가장 긴 증가하는 부분 수열 2
[풀이]
'''
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

from bisect import bisect_left
lst = [A[0]]
for a in A[1:]:
    if lst[-1] < a:
        lst.append(a)
    else:
        idx = bisect_left(lst, a)
        lst[idx] = a
print(len(lst))
