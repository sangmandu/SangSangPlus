'''
https://www.acmicpc.net/problem/1463
1로 만들기
[풀이]
1. 어떤 수 N은 3가지 방법으로 1에 가까워 질 수 있다.
=> -1
=> // 2
=> // 3
2. 따라서 이 3가지 경우 중 매번 최소를 선택하면서 작아지는 경우를 고르면 된다.
3. 또한 이 때, 단순히 나누어 가는게 아닌 N 이하의 수를 모두 검사 해야한다.
'''
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
for m in range(n-1, -1, -1):
    a = b = n
    if m*2 <= n:
        a = dp[m*2]
    if m*3 <= n:
        b = dp[m*3]
    dp[m] = min(a, b, dp[m+1]) + 1
print(dp[1])
