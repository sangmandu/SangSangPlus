'''
https://www.acmicpc.net/problem/9461
파도반 수열
[풀이]
1. 3개의 점화식을 이용해 풀이
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = 0
    b = c = 1
    for _ in range(int(input())):
        a, b, c = b, c, a+b
    print(a)
