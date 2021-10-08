'''
https://www.acmicpc.net/problem/10250
ACM 호텔
[풀이]
'''
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    room, floor = sorted([(a, b) for b in range(1, h+1) for a in range(w)])[n-1]
    print(f'{floor}{room+1:02d}')
    
