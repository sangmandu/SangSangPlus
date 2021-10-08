'''
https://www.acmicpc.net/problem/1436
영화감독 숌
[풀이]
'''
import sys
input = sys.stdin.readline

n = int(input())
num = 665
while n:
    num += 1
    if '666' in str(num):
        n -= 1
print(num)
