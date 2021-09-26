'''
https://www.acmicpc.net/problem/15829
Hashing
[풀이]
'''
import sys
input = sys.stdin.readline

n, st = int(input()), input().strip()
print(sum([(ord(s)-96) * (31 ** i)  for i, s in enumerate(st)]) % 1234567891)
