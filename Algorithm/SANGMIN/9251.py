'''
https://www.acmicpc.net/problem/9251
LCS
[풀이]
1. 두 문자열을 하나씩 비교할 수 있도록 행렬을 만든다.
2. 만약 i번째 문자와 j번째 문자가 같으면 +1을, 다르면 이전값을 받는다.
2-1. 같은 경우
=> 해당 경우는 i-1번째와 j-1번째 까지 비교한 뒤 i번째와 j번째를 비교한 것이다.
=> 따라서 dp[i-1][j-1] 보다 1 크다.
2-2. 다른 경우
=> 해당 경우는 이전 경우의 값을 그대로 받는다. 이 때의 이전의 경우는 2가지이다.
=> dp[i-1][j]와 dp[i][j-1]의 두 가지 경우 중 큰 값을 이어 가진다.
'''
import sys
input = sys.stdin.readline

a, b = input().strip(), input().strip()
sa, sb = len(a)+1, len(b)+1
maxi = 1
dp = [[0] * sb for _ in range(sa)]
for i in range(1, sa):
    for j in range(1, sb):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + (a[i-1] == b[j-1]))
print(dp[-1][-1])
