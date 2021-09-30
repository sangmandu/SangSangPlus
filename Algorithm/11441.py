'''
https://www.acmicpc.net/problem/11441
합 구하기
[풀이]
1. 가로축으로 누적합 구해서 풀기
'''
import sys
input = sys.stdin.readline

from itertools import accumulate
n = int(input())
acc = [0]+list(accumulate(list(map(int, input().split()))))
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(acc[b]-acc[a-1])
    
