'''
https://www.acmicpc.net/problem/11651
좌표 정렬하기 2
[풀이]
'''
import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
for a, b, in sorted(lst, key=lambda x: (x[1], x[0])):
    print(a, b)
