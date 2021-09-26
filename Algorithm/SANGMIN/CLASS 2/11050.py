'''
https://www.acmicpc.net/problem/11050
이항 계수 1
[풀이]
'''
import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())
print(len(list(combinations(range(n), k))))
