'''
https://www.acmicpc.net/problem/2143
두 배열의 합
[풀이]
'''
import sys
input = sys.stdin.readline

T = int(input())
n, A = int(input()), list(map(int, input().split()))
m, B = int(input()), list(map(int, input().split()))

from itertools import accumulate
sa, sb = map(list, [accumulate([0]+A), accumulate([0]+B)])
na = [sa[j]-sa[i] for i in range(n) for j in range(i+1, n+1)]
nb = [sb[j]-sb[i] for i in range(m) for j in range(i+1, m+1)]

from collections import defaultdict
dic = defaultdict(int)
for a in na:
    dic[a] += 1

ans = 0
for b in nb:
    ans += dic[T-b]

print(ans)
