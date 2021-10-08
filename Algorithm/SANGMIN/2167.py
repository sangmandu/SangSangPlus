'''
https://www.acmicpc.net/problem/2167
2차원 배열의 합
[풀이]
1. 배열을 입력받고, 배열의 각 x축에 대해 누적합을 가지고 있는 배열을 또 생성한다.
2. 특정 범위(y1, x1, y2, x2)의 전체합은 (1, 1, y2, x2)에서 (1, 1, y1, x1)을 뺀 범위의 합과 동일하다
'''
import sys
input = sys.stdin.readline

from itertools import accumulate
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cum = [list(accumulate(b)) for b in board]

k = int(input())
for _ in range(k):
    y1, x1, y2, x2 = map(lambda x: int(x)-1, input().split())
    print(sum([cum[y][x2]-cum[y][x1]+board[y][x1] for y in range(y1, y2+1)]))
