'''
https://www.acmicpc.net/problem/10989
수 정렬하기 3
[풀이]
'''
import sys
input = sys.stdin.readline

n = int(input())
cnt = [0 for _ in range(10001)]
for _ in range(n):
    cnt[int(input())] += 1
for i in range(1, 10001):
    for _ in range(cnt[i]):
        print(i)
