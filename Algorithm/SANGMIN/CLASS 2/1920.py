'''
https://www.acmicpc.net/problem/1920
수 찾기
[풀이]
'''
import sys
input = sys.stdin.readline

input()
dic={l:1 for l in list(map(int, input().split()))}
input()
for l in list(map(int, input().split())):
    print(dic.get(l, 0))
