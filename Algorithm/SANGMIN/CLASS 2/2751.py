'''
https://www.acmicpc.net/problem/2751
수 정렬하기 2
[풀이]
'''
import sys
input = sys.stdin.readline

n = int(input())
print(*sorted(list(set([int(input()) for _ in range(n)]))), sep='\n')
