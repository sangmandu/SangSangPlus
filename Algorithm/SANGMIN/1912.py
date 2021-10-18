'''
https://www.acmicpc.net/problem/1912
연속합
[풀이]
1. 연속으로 합을 구하기 위해서는 이전 값에서 계속 현재 값을 더해야 한다.
2. 현재 값을 더할 때, 현재 값 하나를 사용하는 것이 이전 연속합에 더하는 것보다 큰지 비교한다.
'''
import sys
input = sys.stdin.readline

n = int(input())
lst = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = max(dp[i-1], 0) + lst[i]
print(max(dp[1:]))
