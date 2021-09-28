'''
https://www.acmicpc.net/problem/7568
덩치
[풀이]
'''
import sys
input = sys.stdin.readline

n = int(input())
huge = [list(map(int, input().split())) for _ in range(n)]
score = [[huge[idx][0] < huge[jdx][0] and huge[idx][1] < huge[jdx][1] for jdx in range(n)].count(True) for idx in range(n)]
print(*[s+1 for s in score], end=' ')
