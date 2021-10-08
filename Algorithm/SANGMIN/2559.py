'''
https://www.acmicpc.net/problem/2559
수열
[풀이]
1. 부분합의 범위를 정해서 푸는 문제
'''
import sys
input = sys.stdin.readline

from itertools import accumulate
n, k = map(int, input().split())
acc = [0]+list(accumulate(list(map(int, input().split()))))
print(max([acc[idx] - acc[idx-k] for idx in range(k, n+1)]))
