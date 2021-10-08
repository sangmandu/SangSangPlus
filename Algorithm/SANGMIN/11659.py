'''
https://www.acmicpc.net/problem/11659
구간 합 구하기 4
[풀이]
1. 가로축으로 누적합 구해서 풀기
'''
import sys
input = sys.stdin.readline

from itertools import accumulate
n, m = map(int, input().split())
acc = [0]+list(accumulate(list(map(int, input().split()))))

for _ in range(m):
    a, b = map(int, input().split())
    print(acc[b]-acc[a-1])
