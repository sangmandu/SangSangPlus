'''
https://www.acmicpc.net/problem/11047
동전 0
[풀이]
1. 금액이 큰 순서로 검사하는게 당연지사.
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)][::-1]
answer = 0
for coin in coins:
    answer += K // coin
    K = K % coin
print(answer)
