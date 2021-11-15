'''
https://www.acmicpc.net/problem/10816
숫자 카드 2
[풀이]
'''
import sys
input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
lst = list(map(int, input().split()))

from bisect import bisect_left, bisect_right
print(*[bisect_right(cards, item)-bisect_left(cards, item) for item in lst])
