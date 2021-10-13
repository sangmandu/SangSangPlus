'''
https://www.acmicpc.net/problem/2579
계단 오르기
[풀이]
1. 현재 시점 i에서 i-1번째 시점과 i-2번째 시점의 값을 비교한다.
2. i-1번째 시점애서 올 때는 i-2번째 시점을 지나지 않았다는 가정이 필요하다.
=> 따라서, dp[i-1] 이 아닌, dp[i-3]부터 따지게 된다.
'''
import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]
dp = [0] + [sum(stairs[:2])] + [sum(stairs[:3])] + [0] * (n-2)
for i in range(3, n+1):
    a = dp[i-3] + stairs[i-1]
    b = dp[i-2]
    dp[i] = max(a, b) + stairs[i]
print(dp[n])
