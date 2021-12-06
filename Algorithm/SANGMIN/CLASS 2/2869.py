'''
https://www.acmicpc.net/problem/2869
달팽이는 올라가고 싶다
[풀이]
'''
import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())
print((v-a) // (a-b) + (1 if (v-a) % (a-b) else 0) + 1)

