'''
https://www.acmicpc.net/problem/10844
쉬운 계단 수
[풀이]
1. 각 끝자리 마다 만들 수 있는 계단수를 생각해본다.
2. 0은 1, 9는 8로만 만들 수 있고 그 외의 수는 +1, -1해서 2가지를 만들 수 있다.
3. 매번 0~9로 끝나는 수의 개수를 가지고 이를 계산한다.
=> 이는 리스트의 index와 0~9의 수를 매칭한다.
'''
import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for _ in range(n-1):
    dp = [dp[1]] + [dp[i-1] + dp[i+1] for i in range(1, 9)] + [dp[8]]
print(sum(dp) % int(1e+9))
