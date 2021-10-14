'''
https://www.acmicpc.net/problem/11053
가장 긴 증가하는 부분 수열
[풀이]
1. 최소 1의 정답을 가지므로 dp를 1로 초기화
2. 어떤 값 a를 a의 이전의 값들과 비교해야한다.
2-1. 어떤 값 a가 이전의 값들보다 크다.
=> 이전의 값중 제일 최대의 dp를 가지고 있는 애 + 1
2-2. 어떤 값 a가 이전의 값들 중 일부보다 작다.
=> 이전의 값중 내가 얘보다는 크다 하는 얘들을 찾는다
=> 그리고 그 중 제일 최대의 dp를 가지고 있는 애 +1
'''
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
