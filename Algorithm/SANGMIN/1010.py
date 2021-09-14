'''
https://www.acmicpc.net/problem/1010
다리 놓기
[풀이]
1. M개의 점 중 N개를 고르면 자동으로 안겹치게 다리를 놓을 수 있다.
2. for문을 이용하여 combination 적용
'''
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    answer = 1
    for a in range(M, M-N, -1):
        answer *= a
    for a in range(N, 1, -1):
        answer //= a
    print(answer)
