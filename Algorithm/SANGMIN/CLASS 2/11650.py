'''
https://www.acmicpc.net/problem/11650
좌표 정렬하기
[풀이]
'''

import sys
input = sys.stdin.readline

n = int(input())
for a, b in sorted([list(map(int, input().split())) for _ in range(n)]):
    print(a, b)
