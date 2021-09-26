'''
https://www.acmicpc.net/problem/4153
직각삼각형
[풀이]
'''
import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == 0: break
    print("wrong" if a ** 2 + b ** 2 + c ** 2 - 2 * (max(a, b, c) ** 2) else "right")
