'''
https://www.acmicpc.net/problem/10211
Maximum Subarray
[풀이]
'''
import sys
input = sys.stdin.readline

from itertools import accumulate
T = int(input())
for _ in range(T):
    N = int(input())
    X = list(map(int, input().split()))
    lst = list(accumulate([0] + X))
    ans = lst[1]
    for i in range(N):
        for j in range(i+1, N+1):
            ans = max(ans, lst[j]-lst[i])
    print(ans)
